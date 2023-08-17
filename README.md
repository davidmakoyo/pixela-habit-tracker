# Habit Tracker

Habit Tracker is a Python script that lets you create and manage your habit tracking data using the Pixela API. This script allows you to create an account, set up a graph, add data points, and edit/delete existing data points on the graph.

## Getting Started

1. Clone the repository to your local machine.

2. Open the `habit_tracker.py` file in your preferred code editor.

3. Navigate through the code by uncommenting the relevant sections based on the task you want to perform.

## Prerequisites

You'll need to have the `requests` library installed to make HTTP requests. If you don't have it installed, you can install it using:

```
pip install requests
```

## Usage

1. Configure your `USERNAME` and `TOKEN` at the beginning of the script.

2. Uncomment the relevant sections in the script based on the task you want to perform:

   - Creating a user account
   - Creating a habit tracking graph
   - Adding a data point to the graph
   - Editing an existing data point
   - Deleting an existing data point

3. Run the script and observe the console output to see the API responses.

## Example

Here's a brief example of how you can use this script:

1. Uncomment the lines for creating a user account (`user_params` and `user_endpoint`) and set your own user parameters.

2. Run the script. This will create a user account using the provided parameters.

3. Comment out the user account creation lines, uncomment the lines for creating a graph (`graph_params` and `graph_endpoint`), and set your own graph parameters.

4. Run the script again. This will create a graph using the provided parameters.

5. Continue this process for adding, editing, and deleting data points as needed.

## Notes

- Make sure you have valid and unique `USERNAME` and `TOKEN` values.
- Read the Pixela API documentation for more information on request parameters and endpoints.
