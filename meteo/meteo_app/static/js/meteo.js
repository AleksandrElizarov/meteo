//Вычисление background-color для content_param_value
var custom_color_categories = ["#1333ee", "#4febeb", "#dae90e", "#e526eb", "#e45252"];

var limits_temperature = [-10, 5, 20, 30];
set_color_element_by_id(ElementById='temperature', 
                        arr_limits=limits_temperature, 
                        arr_color_cat=custom_color_categories)

var limits_pressure = [900, 950, 1000, 1020, 1040]; 
set_color_element_by_id(ElementById='pressure', 
                        arr_limits=limits_pressure, 
                        arr_color_cat=custom_color_categories) 
                        
var limits_humidity = [10, 25, 40, 65, 85]; 
set_color_element_by_id(ElementById='humidity', 
                        arr_limits=limits_humidity, 
                        arr_color_cat=custom_color_categories) 
                        
var limits_wind_speed = [0, 5, 10, 15, 20];
set_color_element_by_id(ElementById='wind_speed', 
                        arr_limits=limits_wind_speed, 
                        arr_color_cat=custom_color_categories)                         






//Функция опредление background-color по значениям text'a getElementById
function set_color_element_by_id(ElementById, arr_limits, arr_color_cat){
    let element_id = document.getElementById(ElementById);
    let element_text = element_id.textContent;
    if(element_text < arr_limits[0]){
        element_id.style.backgroundColor = arr_color_cat[0];
    } else if((element_text >= arr_limits[0]) && (element_text < arr_limits[1])){
        element_id.style.backgroundColor = arr_color_cat[1];    
    } else if((element_text >= arr_limits[1]) && (element_text < arr_limits[2])){
        element_id.style.backgroundColor = arr_color_cat[2];    
    } else if((element_text >= arr_limits[2]) && (element_text < arr_limits[3])){
        element_id.style.backgroundColor = arr_color_cat[3];    
    } else if(element_text > arr_limits[4]){
        element_id.style.backgroundColor = arr_color_cat[4];    
    }
}

