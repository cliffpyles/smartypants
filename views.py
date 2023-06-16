import random
import time
import rich
import rich_click as click
from rich.progress import Progress, TimeElapsedColumn, SpinnerColumn
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from rich.table import Table
from utils import (
    execute_conversation_command,
    load_completer,
    render_image,
    render_text,
    send_messages_sync,
    send_chat_message_sync,
    send_chat_message_async,
)
from constants import (
    MESSAGE_INDICATOR,
    RESPONSE_INDICATOR,
    SYSTEM_INDICATOR,
)

console = Console()


def view_banner(message):
    click.clear()
    click.echo(message)
    click.echo("Type '/exit' to end the conversation.")


def view_conversations(conversation_files):
    conversations = []
    for file in conversation_files:
        conversation_name, model = file.stem.split("__")
        conversations.append({"name": conversation_name, "model": model})

    if not conversations:
        click.echo("No existing conversations found.")
    else:
        click.echo("Existing conversations:")
        for conversation in conversations:
            click.echo(f"Name: {conversation['name']} | Model: {conversation['model']}")


def view_conversation_async(
    conversation, key_bindings, mac_address, model, session, username
):
    def on_after_add_item(new_message):
        if new_message["role"] == "user":
            view_message(new_message, model)

    def on_after_remove_item(item):
        view_banner(f"Entering an interactive conversation with {model}")
        view_messages(conversation.get_items(), model)

    conversation.register_event_hook("after", "add_item", on_after_add_item)
    conversation.register_event_hook("after", "remove_item", on_after_remove_item)

    view_banner(f"Entering an interactive conversation with {model}")
    view_messages(conversation.get_items(), model)

    current_state = {
        "mac_address": mac_address,
        "model": model,
        "multiline_mode": False,
        "username": username,
    }

    while True:
        completer = load_completer(conversation)

        user_input = session.prompt(
            message=f"\n\n{MESSAGE_INDICATOR} New Message: ",
            key_bindings=key_bindings,
            multiline=current_state.get("multiline_mode", False),
            wrap_lines=True,
            completer=completer,
        )

        # Execute the command if the input starts with a '/'
        if user_input.startswith("/"):
            conversation, current_state, user_input = execute_conversation_command(
                user_input,
                conversation=conversation,
                current_state=current_state,
                user_input=user_input,
            )
            if "warnings" in current_state:
                for warning in current_state["warnings"]:
                    click.secho(warning, fg="yellow")
                del current_state["warnings"]
            if "notifications" in current_state:
                for notification in current_state["notifications"]:
                    click.secho(notification, fg="blue")
                del current_state["notifications"]
        elif len(user_input.strip()) > 0:
            try:
                user_message = conversation.add_item(
                    {
                        "role": "user",
                        "name": username,
                        "content": f"{user_input}",
                        "mac_address": mac_address,
                    }
                )
                messages = conversation.get_items()
                response_generator = send_chat_message_async(
                    model=model, messages=messages, user_message=user_message
                )
                response_message = view_response_stream(response_generator)
                assistant_message = {"role": "assistant", "content": response_message}
                conversation.add_item(assistant_message)
                current_state["multiline_mode"] = False
            except Exception as e:
                click.echo(f"Error: {e}")


def view_conversation_sync(
    conversation, key_bindings, mac_address, model, session, username
):
    def on_after_add_item(new_message):
        view_message(new_message, model)

    def on_after_remove_item(item):
        view_banner(f"Entering an interactive conversation with {model}")
        view_messages(conversation.get_items(), model)

    conversation.register_event_hook("after", "add_item", on_after_add_item)
    conversation.register_event_hook("after", "remove_item", on_after_remove_item)

    view_banner(f"Entering an interactive conversation with {model}")
    view_messages(conversation.get_items(), model)

    current_state = {
        "mac_address": mac_address,
        "model": model,
        "multiline_mode": False,
        "username": username,
    }

    while True:
        completer = load_completer(conversation)

        user_input = session.prompt(
            message=f"\n\n{MESSAGE_INDICATOR} New Message: ",
            key_bindings=key_bindings,
            multiline=current_state.get("multiline_mode", False),
            wrap_lines=True,
            completer=completer,
        )

        # Execute the command if the input starts with a '/'
        if user_input.startswith("/"):
            conversation, current_state, user_input = execute_conversation_command(
                user_input,
                conversation=conversation,
                current_state=current_state,
                user_input=user_input,
            )
            if "warnings" in current_state:
                for warning in current_state["warnings"]:
                    click.secho(warning, fg="yellow")
                del current_state["warnings"]
            if "notifications" in current_state:
                for notification in current_state["notifications"]:
                    click.secho(notification, fg="blue")
                del current_state["notifications"]
            if "send_messages" in current_state:
                try:
                    messages = conversation.get_items()
                    get_api_data = lambda: send_messages_sync(
                        model=model, messages=messages
                    )
                    response_message = view_data_loader(fn=get_api_data)
                    assistant_message = response_message.to_dict_recursive()
                    conversation.add_item(assistant_message)
                    current_state["multiline_mode"] = False
                    del current_state["send_messages"]
                except Exception as e:
                    click.echo(f"Error: {e}")

        elif len(user_input.strip()) > 0:
            try:
                user_message = conversation.add_item(
                    {
                        "role": "user",
                        "name": username,
                        "content": f"{user_input}",
                        "mac_address": mac_address,
                    }
                )
                messages = conversation.get_items()
                get_api_data = lambda: send_chat_message_sync(
                    model=model, messages=messages, user_message=user_message
                )
                # response_message = send_chat_message_sync(model, messages, user_message)
                response_message = view_data_loader(fn=get_api_data)
                assistant_message = response_message.to_dict_recursive()
                conversation.add_item(assistant_message)
                current_state["multiline_mode"] = False

            except Exception as e:
                click.echo(f"Error: {e}")


def view_data_loader(fn, **kwargs):
    with Progress(
        SpinnerColumn(),
        TimeElapsedColumn(),
    ) as progress:
        loading_task = progress.add_task("[green]Processing…", total=None)
        response = fn()
        progress.update(loading_task, completed=True, visible=False)

    return response


def view_image(image_description, image_url, size):
    render_text(f"Description: {image_description}\n")
    render_text(f"Size: {size}x{size}\n")
    render_text(f"Preview URL: {image_url}\n")
    render_image(image_url)


def view_message(message, model="Unknown", raw=False):
    message_id = message.get("id", None)
    if message["role"] == "user":
        click.secho(f"\n\n{MESSAGE_INDICATOR} Message:\n", bold=True)
    elif message["role"] == "system":
        click.secho(f"\n\n{SYSTEM_INDICATOR} System:\n", bold=True)
    elif message["role"] == "assistant":
        click.secho(f"\n\n{RESPONSE_INDICATOR} Response:\n", bold=True)

    if raw:
        click.echo(message["content"])
    else:
        markdown = Markdown(message["content"])
        console.print(markdown)

    usage_label = ""

    if message["role"] == "assistant":
        usage_label += f" | model: {model}"

    if "usage" in message:
        prompt_tokens = message.get("usage").get("prompt_tokens")
        completion_tokens = message.get("usage").get("completion_tokens")
        total_tokens = message.get("usage").get("total_tokens")
        token_limits = {"gpt-3.5-turbo": "4096", "gpt-4": "8192"}
        token_limit = token_limits.get(model, "Unknown")
        usage_label += " | message: "
        usage_label += f"{prompt_tokens}"
        usage_label += " tokens"

        usage_label += " | response: "
        usage_label += f"{completion_tokens}"
        usage_label += " tokens"

        usage_label += " | total: "
        usage_label += f"{total_tokens}"
        usage_label += "/"
        usage_label += f"{token_limit}"
        usage_label += " tokens"

    if message["role"] == "assistant":
        divider_label = (
            f"{RESPONSE_INDICATOR} {message_id}{usage_label}" if message_id else ""
        )
        click.echo("\n")
        console.rule(f"{divider_label}", align="center")
        click.echo("\n")
    elif message["role"] == "user":
        divider_label = (
            f"{MESSAGE_INDICATOR} {message_id}{usage_label}" if message_id else ""
        )
        click.echo("\n")
        console.rule(f"{divider_label}", align="center")
        click.echo("\n")


def view_messages(messages, model="Unknown", raw=False):
    for message in messages:
        view_message(message, model, raw)


def view_prompts(prompts):
    if not prompts:
        click.echo("No available prompts.")
    else:
        prompts = sorted(prompts, key=lambda i: i["keys"][0])
        table = Table(title="Prompts")
        table.add_column("Name", no_wrap=True)
        table.add_column("Aliases")
        table.add_column("Model")
        table.add_column("System Context")
        for prompt in prompts:
            keys = prompt.get("keys")
            model = prompt.get("model")
            messages = prompt.get("messages")
            name = keys[0]
            aliases = ", ".join(keys[1:])
            first_message_role = messages[0]["role"]
            first_message_content = messages[0]["content"]
            system_context = ""
            if first_message_role == "system":
                system_context = first_message_content
            table.add_row(name, aliases, model, system_context)
        console.print(table)


def view_response_stream(response_generator, raw=False):
    all_lines = ""
    line = ""
    if not raw:
        click.secho(f"\n\n{RESPONSE_INDICATOR} Response:\n", bold=True)
        with Live(refresh_per_second=10) as live:
            for message in response_generator:
                finish_reason = message["choices"][0]["finish_reason"]
                if finish_reason == "stop":
                    markdown = Markdown(all_lines)
                    live.update(markdown)
                    break
                else:
                    delta = message["choices"][0]["delta"]
                    content = delta.get("content", "")
                    all_lines += content
                    markdown = Markdown(all_lines)
                    live.update(markdown)
    else:
        for message in response_generator:
            finish_reason = message["choices"][0]["finish_reason"]
            if finish_reason == "stop":
                click.echo(line)
                break
            else:
                delta = message["choices"][0]["delta"]
                content = delta.get("content", "")
                line += content
                all_lines += content
                if "\n" in content:
                    click.echo(line)
                    line = ""
    return all_lines


def view_edit_sync(file, key_bindings, mac_address, messages, model, session, username):
    current_state = {
        "mac_address": mac_address,
        "model": model,
        "multiline_mode": False,
        "username": username,
        "running": True,
    }
    view_banner(f"Editing {file.name} with {model}")
    view_messages(messages, model)
    while current_state["running"]:
        user_input = session.prompt(
            message=f"\n\n{MESSAGE_INDICATOR} New Message: ",
            key_bindings=key_bindings,
            multiline=current_state.get("multiline_mode", False),
            wrap_lines=True,
        )

        # Execute the command if the input starts with a '/'
        if user_input.startswith("/exit"):
            current_state["running"] = False
        elif user_input.startswith("/multi"):
            current_state["multiline_mode"] = True
        elif len(user_input.strip()) > 0:
            try:
                user_message = {
                    "role": "user",
                    "name": username,
                    "content": f"{user_input}",
                    "mac_address": mac_address,
                }
                get_api_data = lambda: send_chat_message_sync(
                    model=model, messages=messages, user_message=user_message
                )
                response_message = view_data_loader(fn=get_api_data)
                assistant_message = response_message.to_dict_recursive()
                rendered_content = Markdown(assistant_message["content"])
                console.print(rendered_content)
                if "```" in assistant_message["content"]:
                    confirm_apply = click.confirm("Do you want to apply the changes?")
                    if confirm_apply:
                        messages.append(user_message)
                        messages.append(assistant_message)
                        stripped_text = (
                            assistant_message["content"].strip().strip("```").strip()
                        )
                        file.write_text(f"{stripped_text}\n")
                current_state["multiline_mode"] = False
            except Exception as e:
                click.echo(f"Error: {e}")


def view_conversation_output(conversation, model):
    view_messages(conversation.get_items(), model)
