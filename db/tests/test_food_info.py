import db.food_info as fi

def test_get_food_info():
	foodInfoList = fi.get_food_info()
	assert isinstance(foodInfoList, list)
	assert len(foodInfoList) > 1

def test_get_food_info_details():
	foodDetailsDict = fi.get_food_info_details("APPLE PIE")
	assert isinstance(foodDetailsDict, dict)
	assert len(foodDetailsDict) > 1
