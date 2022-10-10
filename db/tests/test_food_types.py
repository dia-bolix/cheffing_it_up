import cheffing_it_up.db.food_types as ft

def test_get_food_types():
	food_type_list = ft.get_food_types()
	assert isinstance(food_type_list, list)
	assert len(food_type_list) > 1

def test_get_food_info_details():
	food_details_dict = ft.get_food_type_details("APPLE PIE")
	assert isinstance(food_details_dict, dict)
	assert len(food_details_dict) > 1
