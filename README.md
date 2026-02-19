# E-Commerce Inventory Management Backend Task

## Task Overview
ShopFlow is an e-commerce platform managing products across multiple suppliers, categories, and warehouses. Your task is to design the PostgreSQL schema and implement database logic for a FastAPI application that handles complex inventory workflows, such as stock tracking per warehouse, price changes with historical tracking, low-stock detection, movement logging, and purchase order processing. Implementing both the normalized schema and async FastAPI integration is essential to ensure ShopFlow operates reliably, scales for high concurrency, and maintains correct real-time inventory data for business continuity and growth.

## Objectives
- Create a lightweight schema that defines products, basic categories, warehouses, and inventory records in a clear relational structure.
- Establish essential relationships so that product and inventory information remain consistent across the system.
- Seed the database with a small but meaningful dataset that enables product listing, category filtering, and simple inventory checks.
- Ensure FastAPI endpoints interact with the database using asynchronous operations for smooth request handling.
- Include a simple mechanism to record inventory adjustments so that changes can be traced during verification.
- Maintain reliable behavior in core workflows such as product retrieval and stock updates.

## Database Access
- **Host:** `<DROPLET_IP>`
- **Port:** 5432
- **Database:** shopflow
- **User:** shopuser
- **Password:** shoppass

You may connect directly with psql/DBeaver/pgAdmin for DB access. Test implemented endpoints via Postman or curl as you build out async logic.

## How to Verify
- Load your schema and sample data into the database and inspect the tables to ensure they reflect the intended structure.
- Use the provided API endpoints to confirm that product listings, category filters, and basic searches return consistent results.
- Update inventory for a product and check that the change is reflected correctly in both the API responses and the database records.
- Test a few invalid or boundary conditions—such as negative quantities or unknown categories—to confirm that the system responds meaningfully.
- Review any tracking records for inventory adjustments to ensure they provide clear and useful information about changes.
- Perform a small number of concurrent requests to validate that the API remains responsive and that data consistency is preserved.

## Helpful Tips
- Explore the existing FastAPI project structure in `/root/task/app/` to understand how routing and database access are organized.
- Review the empty SQL files provided for schema and initial data; your task is to create a concise structure that supports basic product and inventory operations.
- All database interactions in the FastAPI routes rely on async-compatible SQL helpers, so keep non-blocking patterns in mind when designing your data model.
- Focus on the core flow: listing products, checking available stock, and updating inventory during standard operations.
- Think through how inventory adjustments should be tracked so that the system preserves meaningful state after each update.
- Consider how simple indexing or relationship design can help common lookups behave more predictably.
