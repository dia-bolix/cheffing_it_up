# demo-repo3

An example flask rest API server, for SE Fall 2022.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

We will be making a cookbook API which stores recipes.

## Requirements

- Store recipes
- Get recipes
- Get recipes by type/time of day
- Share recipes (with a link or txt file)
- Search for a recipe
- Adding images to a recipe
- Enter in ingredients and return a set of recipes
- Option to Sort by recipe price based on prices from large retailer (Walmart)
- Option to Sort food items seasonly
- Add a section of recipes by famous chefs
 Design
Each of the main components above will corresponded to an API endpoint. 
We wil source our price data from Walmart or some larger national food cost database for our information. Will also have to source images from the web.



