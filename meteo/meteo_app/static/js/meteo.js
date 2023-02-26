//Вычисление background-color для content_param_value
const custom_color_categories = ["#586ada", "#78e0e0", "#88cc6d", "#d9a673", "#dc6f6f"];

const limits_temperature = [-10, 5, 20, 30];
set_color_element_by_id(ElementById = 'temperature',
    arr_limits = limits_temperature,
    arr_color_cat = custom_color_categories)

//Функция опредление background-color по значениям text'a getElementById
function set_color_element_by_id(ElementById, arr_limits, arr_color_cat) {
    let element_id = document.getElementById(ElementById);
    let element_text = element_id.textContent;
    if (element_text < arr_limits[0]) {
        element_id.style.backgroundColor = arr_color_cat[0];
    } else if ((element_text >= arr_limits[0]) && (element_text < arr_limits[1])) {
        element_id.style.backgroundColor = arr_color_cat[1];
    } else if ((element_text >= arr_limits[1]) && (element_text < arr_limits[2])) {
        element_id.style.backgroundColor = arr_color_cat[2];
    } else if ((element_text >= arr_limits[2]) && (element_text < arr_limits[3])) {
        element_id.style.backgroundColor = arr_color_cat[3];
    } else if (element_text > arr_limits[3]) {
        element_id.style.backgroundColor = arr_color_cat[4];
    }
}

//Вычисление направления ветра(юг, север, запад, восток и т.д. в зависимости от направления азимута в градусах)
const directions = ['Север.', 'СВ', 'Восточ.', 'ЮВ', 'Южн.', 'ЮЗ', 'Запад.', 'СЗ'];
let element_wind_deg = document.getElementById('wind_deg');
let angle = document.getElementById('wind_deg').textContent;
let index = Math.round(((angle %= 360) < 0 ? angle + 360 : angle) / 45) % 8;
element_wind_deg.innerText = directions[index];


