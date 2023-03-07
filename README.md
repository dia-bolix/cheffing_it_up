# Cheffing It Up

An example flask rest API server, for SE Fall 2022.

[Front End](https://github.com/alstonS/cheffing_it_up_client)

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

We will be making a cookbook API which stores recipes.

## Requirements

### User endpoints:
- Add a user (signup)
- List current users
- Delete a user

### Food types endpoints:
- List food types (breakfast, lunch, dinner)
- Show details about food types

### Food menu endpoints:
- Add a recipe
- Search for a recipe
- Get a recipe by type/time of day
- Store recipes
- Share recipes (with a link or txt file)
- Adding images to a recipe
- Enter in ingredients and return a set of recipes
- Option to Sort by recipe price based on prices from large retailer (Walmart)
- Option to Sort food items seasonlly
- Add a section of recipes by famous chefs

## Design
Each of the main components above will corresponded to an API endpoint. 
We wil source our price data from Walmart or some larger national food cost database for our information. Will also have to source images from the web.