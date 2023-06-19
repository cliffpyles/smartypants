# Overview

The AI Services Interaction Suite is a comprehensive system that allows users to interact with AI services, particularly OpenAI, across a suite of applications and tools. The system is architected around serverless AWS services, providing scalable, performant, and cost-effective solutions.

## Core Components

- **[CLI Tool](cli-spec.md)**: A CLI app for advanced users, which supports a variety of commands for interacting with AI services.
- **[GraphQL API](api-spec.md)**: A GraphQL API built with AWS AppSync, providing a flexible interface for web and mobile applications.
- **[Web Application](web-ui-spec.md)**: A Single Page Application (SPA) built with React.js, offering an interactive interface for users to engage with the AI services.

## Event-Driven Architecture

The system uses an event-driven architecture, where changes to the data (in DynamoDB) trigger a series of Lambda functions that interact with the AI services and update the data accordingly. It employs AWS EventBridge as the event hub, managing the flow of events between services. [More Info](event-driven-architecture.md)

## Domain-Driven Design

The design of the system follows the principles of Domain-Driven Design (DDD), with clearly defined contexts, entities, value objects, and aggregates. [More Info](domain-driven-design.md)

## Product Specification

The product is a comprehensive suite for interacting with a variety of AI services. It extends the functionality of these AI services and provides a single interface to them. It includes a CLI app, a web app, a mobile app, and a GraphQL API. [More Info](product-spec.md)

## AWS Well-Architected Framework

The system design adheres to the five pillars of the AWS Well-Architected Framework - Operational Excellence, Security, Reliability, Performance Efficiency, and Cost Optimization. [More Info](aws-well-architected-framework.md)

## Cost Analysis

An estimate of the costs involved in running this system has been provided, based on the services used and possible usage scenarios. [More Info](cost-analysis.md)
