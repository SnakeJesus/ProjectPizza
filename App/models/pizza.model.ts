import { ImgHTMLAttributes } from "react";
import { Float } from "react-native/Libraries/Types/CodegenTypes";

export interface Pizza {
    crust: Float,
    sauce: string,
    plate: string,
    toppings: [
        topping: string
    ],
    uid: string
}