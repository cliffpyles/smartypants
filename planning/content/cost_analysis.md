# Cost Analysis

**_Cost of AWS services vary by region, usage, and configuration, so it's crucial to check the most recent pricing details on the AWS website. This is only meant for use as educated guesses._**

## Cost Structures

1. **Amazon DynamoDB:** Costs for DynamoDB depend on the amount of read and write capacity units you provision. There are also costs for data storage, data transfer, and optional features like DynamoDB Streams or Global Tables. For instance, in the US East Region, the first 25GB of storage is free, after which you pay $0.25 per GB-month.

2. **AWS Lambda:** With Lambda, you pay for execution duration rather than by server unit. Pricing depends on the amount of memory you allocate to your functions and the number of requests. As of my knowledge cutoff in September 2021, the first 1 million requests per month are free, after which you pay $0.20 per 1 million requests ($0.0000002 per request).

3. **Amazon API Gateway:** For REST APIs, you pay $3.50 per million API calls received, plus the cost of data transfer out. The first 500MB of data transfer out per month is free.

4. **AWS Amplify:** Amplify's costs depend on your usage of its various features, like build & deploy, hosting, or backend environment. For instance, hosting costs $0.023 per GB served for the first 10TB.

5. **Amazon AppSync:** With AppSync, you pay for the number of query and data modification operations your application makes, the data transferred out, and, optionally, caching capacity. Query and data modification costs $4.00 per million.

6. **Amazon EventBridge:** EventBridge pricing is mainly based on the number of events you generate, with the first 5 million events per month being free, and $1.00 per million events thereafter.

7. **Amazon Cognito:** With Cognito, your costs are based on your monthly active users (MAUs), and it starts with a free tier of 50,000 MAUs for the pool of users who sign in with Cognito User Pools.

Here's a high-level summary of costs for the primary services used in your architecture, along with some example usage scenarios. Please note these are illustrative examples based on standard pricing and may vary depending on the region and specific workload characteristics. It's always recommended to use the AWS Pricing Calculator for precise estimates.

---

## Services Used

- **Amazon DynamoDB:** Cost based on provisioned read and write capacity units, storage, and optional features.
- **AWS Lambda:** Pay per execution, dependent on memory allocated and number of requests.
- **Amazon API Gateway:** Pay per API call received, and data transfer out.
- **AWS Amplify:** Pay based on usage of build & deploy, hosting, or backend environment features.
- **Amazon AppSync:** Pay for number of query and data modification operations, data transfer, and optional caching.
- **Amazon EventBridge:** Pricing mainly based on the number of events generated.
- **Amazon Cognito:** Cost based on your monthly active users (MAUs).

## Example Usage Scenarios

1. **Startup Phase:**

- DynamoDB: Minimal read/write capacity and storage (mostly within free tier).
- Lambda: Limited executions, mostly within the free tier.
- API Gateway: Limited API calls (mostly within free tier).
- Amplify: Minimal backend usage and hosting. Few builds and deploys.
- AppSync: Minimal operations and transfer (mostly within free tier).
- EventBridge: Few events, mostly within free tier.
- Cognito: Under 50,000 MAUs.

**Estimated Cost: Low, possibly within free tier limits.**

2. **Growth Phase:**

- DynamoDB: Increased read/write capacity and storage due to higher usage.
- Lambda: Increased executions as traffic grows.
- API Gateway: Increased API calls due to increased usage.
- Amplify: Increased backend usage and hosting. More frequent builds and deploys.
- AppSync: More operations and transfer due to increased user interactions.
- EventBridge: More events as application functionality grows.
- Cognito: MAUs growing, but under 50,000.

**Estimated Cost: Moderate, moving beyond free tier limits.**

3. **Scale Phase:**

- DynamoDB: High read/write capacity and storage for substantial user base.
- Lambda: High number of executions due to high traffic.
- API Gateway: High API calls due to large user base.
- Amplify: High backend usage and hosting. Frequent builds and deploys.
- AppSync: High number of operations and data transfer due to heavy user interactions.
- EventBridge: Large number of events as application complexity increases.
- Cognito: MAUs in high tens of thousands or more.

**Estimated Cost: High, a significant part of operational costs.**

Remember that many of these services offer savings plans, reserved capacity, or other pricing models that can help control costs as your usage grows. Please check the latest AWS pricing documentation or use the AWS Pricing Calculator for the most accurate information.

---

Sure, let's combine the detailed service costs analysis and the usage scenarios into one coherent summary. Note that these are estimations and can vary widely depending on your exact usage patterns, regions, and other factors.

## Cost Analysis Summary

**Services:**

- **Amazon DynamoDB:** Pay for the data read/write capacity you provision, the storage you consume, and any optional features like global tables or backups.
- **AWS Lambda:** Pay for the number of requests and the duration of code execution, calculated in GB-seconds.
- **Amazon API Gateway:** Pay per million API calls received and the amount of data transferred out.
- **AWS Amplify:** Costs are based on the usage of build and deploy features, hosting, and backend environment features.
- **Amazon AppSync:** Pay for the number of query and data modification operations, the amount of data transferred, and optional caching.
- **Amazon EventBridge:** Main cost is based on the number of events ingested, processed, or delivered by the service.
- **Amazon Cognito:** Pay per monthly active user, which varies based on the features used.

**Usage Scenarios:**

1. **Startup Phase:**

   In the startup phase, your costs are likely to be low as your traffic is still growing. Most services might fall within the AWS free tier, leading to minimal costs.

2. **Growth Phase:**

   As your application's usage grows, so does the cost. As you move out of the free tier, you'll start paying for the increased usage of services like DynamoDB, Lambda, API Gateway, Amplify, AppSync, EventBridge, and Cognito.

3. **Scale Phase:**

   At scale, your costs will increase significantly. You'll be handling high traffic, leading to a lot of Lambda executions, API calls, data read/write operations, and events. User management costs with Cognito will also grow as you handle more monthly active users.

**Estimations:**

- **Startup Phase Estimated Cost:** Low, possibly within free tier limits.
- **Growth Phase Estimated Cost:** Moderate, moving beyond free tier limits.
- **Scale Phase Estimated Cost:** High, a significant part of operational costs.

Remember to consider cost optimization techniques such as right-sizing, increasing efficiency, using saving plans, and taking advantage of AWS cost management tools. For the most accurate information, please use the AWS Pricing Calculator or consult the latest AWS pricing documentation.
