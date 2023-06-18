# Bounded Contexts

1. **Core**: The basic functionality provided by SmartyPants itself, including features such as displaying the version of the tool. This context is separate from the plugin contexts as it pertains to functionality provided directly by the CLI tool, not through a plugin.

2. **OpenAI**: This context encapsulates all functionality related to interacting with OpenAI. It includes the ability to chat, draw, manage models and prompts, and send messages.

3. **Plugins**: This context deals with managing plugins themselves - enabling, disabling, installing, listing, uninstalling, updating, and viewing the status of plugins. It is separate from the other contexts as it manages meta-functionality related to plugins themselves, not the specific actions those plugins enable.

These bounded contexts each have their own models, rules, and behaviors, and while they interact, they can also evolve independently.
