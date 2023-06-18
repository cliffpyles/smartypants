# Architecture

## System Components

```mermaid
graph LR
  A[Client] -- GraphQL --> B(Amplify)
  B -- DynamoDB --> C(DynamoDB)
  C -- Trigger --> D1(Lambda: DDB Trigger Handler)
  D1 -- Publish --> E(EventBridge)
  E -- Subscribe --> D2(Lambda: Event Handlers)
  D2 -- request --> F(OpenAI API)
  D2 -- update --> C
```

## Event Flow

```mermaid
sequenceDiagram
  participant User as User
  participant Amplify as Amplify
  participant DynamoDB as DynamoDB
  participant DDBTrigger as Lambda (DDB Trigger Handler)
  participant EventBridge as EventBridge
  participant EventHandler as Lambda (Event Handlers)
  participant OpenAI as OpenAI API
  User->>Amplify: Create/Update (Chat/Message)
  Amplify->>DynamoDB: Write operation
  DynamoDB->>DDBTrigger: Trigger event
  DDBTrigger->>EventBridge: Publish event
  EventBridge->>EventHandler: Dispatch event
  EventHandler->>OpenAI: Sends data
  OpenAI->>EventHandler: Returns response
  EventHandler->>DynamoDB: Update operation
```

## Data Model

```mermaid
classDiagram
  class User {
    +ID: ID!
    +username: String!
    +chats: [Chat]!
  }
  class Chat {
    +ID: ID!
    +name: String!
    +owner: User!
    +access: String!
    +messages: [Message]!
  }
  class Message {
    +ID: ID!
    +content: String!
    +chat: Chat!
    +owner: User!
    +access: String!
  }
  User "1" --> "*" Chat: owns
  User "1" --> "*" Message: owns
  Chat "1" --> "*" Message: contains

```
