# SmartyPants CLI Tool

Welcome to SmartyPants, a user-friendly CLI tool for interacting with AI services, featuring a powerful command and plugin system!

## Contents

1. [Setup](#setup)
2. [Usage](#usage)
3. [Plugins](#plugins)
    
    - [Plugins](#Plugins)
    
    - [OpenAI](#OpenAI)
    
4. [Contributor Guidelines](#contributor-guidelines)
5. [Licenses and Legal](#licenses-and-legal)

## Setup

### Requirements

_no requirements specified_

### Installation

**Homebrew**

`brew install smartypants-cli`

**NPM**

`npm install -g smartypants-cli`

**PIP**

`pip install smartpants-cli`


## Usage

`smartypants <plugin_name> <plugin_command> [arguments] [options]`


## Plugins


### Plugins


**Command:** `disable` Disables a plugin

**Usage:** `smartypants plugins <arguments>`

#### Arguments



`plugin` (Required): Name of plugin



#### Options



#### Examples



_Disable a plugin_
```bash
smartypants plugins disable openai
```




**Command:** `enable` Enables a plugin

**Usage:** `smartypants plugins <arguments>`

#### Arguments



`plugin` (Required): Name of plugin



#### Options



#### Examples



_Enable a plugin_
```bash
smartypants plugins enable openai
```




**Command:** `install` Installs a plugin

**Usage:** `smartypants plugins <arguments>`

#### Arguments



`plugin` (Required): Name of plugin



#### Options



#### Examples



_Install a plugin_
```bash
smartypants plugins install openai
```




**Command:** `list` Lists all installed plugins

**Usage:** `smartypants plugins`

#### Arguments



#### Options



#### Examples



_List all installed plugins_
```bash
smartypants plugins list
```




**Command:** `uninstall` Uninstalls a plugin

**Usage:** `smartypants plugins <arguments>`

#### Arguments



`plugin` (Required): Name of plugin



#### Options



#### Examples



_Uninstall a plugin_
```bash
smartypants plugins uninstall openai
```




**Command:** `update` Updates a plugin

**Usage:** `smartypants plugins <arguments>`

#### Arguments



`plugin` : Name of plugin



#### Options



#### Examples



_Update a plugin_
```bash
smartypants plugins update openai
```




**Command:** `status` Shows state of a specific plugin

**Usage:** `smartypants plugins <arguments>`

#### Arguments



`plugin` : Name of plugin



#### Options



#### Examples



_Show status of a plugin_
```bash
smartypants plugins status openai
```





### OpenAI


**Command:** `chat` An interactive session with OpenAI

**Usage:** `smartypants openai`

#### Arguments



#### Options



#### Examples




**Command:** `models` List available models

**Usage:** `smartypants openai`

#### Arguments



#### Options



#### Examples



_List available models in OpenAI_
```bash
smartypants openai models
```




**Command:** `prompts` Preconfigured prompt to use with chats

**Usage:** `smartypants openai`

#### Arguments



#### Options



#### Examples




**Command:** `send` Send one or more messages to OpenAI

**Usage:** `smartypants openai [options]`

#### Arguments



#### Options



`attach` : File to include as message

`live` : Stream the response as it is received

`message` : Message to send

`model` (Default: gpt-3.5-turbo): Language model to use

`raw` : Don't format the response



#### Examples



_Send one or more messages to OpenAI_
```bash
smartypants openai send --message 'Hello OpenAI' --model 'gpt-3.5-turbo'
```






## Contributor Guidelines



## Licenses and Legal

