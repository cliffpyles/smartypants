#!/usr/bin/env python3

import rich_click as click
from constants import VALID_ASK_MODELS, VALID_CONVERSATION_MODELS
from commands import (
    ask_command,
    conversation_command,
    delete_command,
    draw_command,
    edit_command,
    fork_command,
    list_command,
    models_command,
    prompts_command,
    send_command,
    show_command,
)


@click.group()
def main():
    pass


@main.command()
@click.argument("user_input", type=str, required=True)
@click.option(
    "-m",
    "--model",
    type=click.Choice(VALID_ASK_MODELS),
    help=f"Language model to use. Valid models: {', '.join(VALID_ASK_MODELS)}",
)
@click.option(
    "-p",
    "--prompt",
    type=str,
    default="default",
    help="Name of a preconfigured prompt to use",
)
@click.option("-r", "--raw", is_flag=True, help="Show the raw content")
@click.option(
    "-s", "--stream", is_flag=True, help="Whether the response should be streamed."
)
def ask(user_input, **kwargs):
    """Ask a single question to the chatbot"""
    ask_command(user_input, **kwargs)


@main.command()
@click.argument("conversation_name", type=str)
@click.option(
    "-m",
    "--model",
    type=click.Choice(VALID_CONVERSATION_MODELS),
    help=f"Language model to use. Valid models: {', '.join(VALID_CONVERSATION_MODELS)}",
)
@click.option(
    "-p",
    "--prompt",
    type=str,
    default="default",
    help="Name of a preconfigured prompt to use",
)
@click.option(
    "-s", "--stream", is_flag=True, help="Whether the responses should be streamed."
)
def conversation(**kwargs):
    """Start an ongoing conversation with the chatbot"""
    conversation_command(**kwargs)


@main.command()
@click.argument("conversation_name", type=str)
@click.option(
    "-m",
    "--model",
    type=click.Choice(VALID_CONVERSATION_MODELS),
    default=VALID_CONVERSATION_MODELS[0],
    help=f"Language model to use. Valid models: {', '.join(VALID_CONVERSATION_MODELS)}",
)
@click.option(
    "-f", "--force", is_flag=True, help="Force deletion without confirmation."
)
def delete(**kwargs):
    """Delete a conversation"""
    delete_command(**kwargs)


@main.command()
@click.argument("image_description", type=str)
@click.option("-b", "--browser", is_flag=True, help="Opens image in a new browser tab.")
@click.option(
    "-s",
    "--size",
    type=click.Choice(["256", "512", "1024"]),
    default="256",
    help="Size of the image in pixels.",
)
def draw(**kwargs):
    """Draw an image based on a description"""
    draw_command(**kwargs)


@main.command()
@click.argument("filepath", type=str)
@click.option(
    "-m",
    "--model",
    type=click.Choice(VALID_CONVERSATION_MODELS),
    help=f"Language model to use. Valid models: {', '.join(VALID_CONVERSATION_MODELS)}",
)
@click.option("-r", "--raw", is_flag=True, help="Show the raw content")
def edit(**kwargs):
    """Start an ongoing edit with the chatbot"""
    edit_command(**kwargs)


@main.command()
@click.argument("source_conversation_name", type=str)
@click.argument("new_conversation_name", type=str)
@click.option(
    "-m",
    "--model",
    type=click.Choice(VALID_CONVERSATION_MODELS),
    default=VALID_CONVERSATION_MODELS[0],
    help=f"Language model to use. Valid models: {', '.join(VALID_CONVERSATION_MODELS)}",
)
def fork(**kwargs):
    """Duplicate an existing conversation"""
    fork_command(**kwargs)


@main.command()
def list(**kwargs):
    """List existing conversations"""
    list_command(**kwargs)


@main.command()
def models(**kwargs):
    """Show the available models"""
    models_command(**kwargs)


@main.command()
def prompts(**kwargs):
    """Lists preconfigured prompts"""
    prompts_command(**kwargs)


@main.command()
@click.argument("filepath", type=str)
@click.option(
    "-a", "--apply", is_flag=True, help="Apply the response to the prompt file"
)
@click.option(
    "-i", "--interactive", is_flag=True, help="Ask if you want to the apply response"
)
@click.option("-r", "--raw", is_flag=True, help="Show the raw content")
@click.option(
    "-s", "--stream", is_flag=True, help="Whether the response should be streamed"
)
def send(**kwargs):
    """Sends the prompt at the given filepath"""
    send_command(**kwargs)


@main.command()
@click.argument("conversation_name", type=str)
@click.option(
    "-m",
    "--model",
    type=click.Choice(VALID_CONVERSATION_MODELS),
    default=VALID_CONVERSATION_MODELS[0],
    help=f"Language model of conversation. Valid models: {', '.join(VALID_CONVERSATION_MODELS)}",
)
def show(**kwargs):
    """Shows a previous conversation"""
    show_command(**kwargs)


if __name__ == "__main__":
    main()
