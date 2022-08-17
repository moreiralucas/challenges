import axios, { AxiosRequestConfig, AxiosResponse } from "axios";


// eslint-disable-next-line prefer-const
let http = axios.create({
    baseURL: "http://localhost:5000",
    headers: {},
});

const services = {
    api: {
        v1: {
            getHeroes: async (
                page: number | string = 1,
                page_size: number | string = 5,
                ordering = "",
                search = "",
                config: AxiosRequestConfig = {}
            ): Promise<AxiosResponse> => {
                const url = `/api/v1/hero/?page=${page.toString()}&page_size=${page_size.toString()}&ordering=${ordering}&search=${search}`;
                return await http.get(url, config);
            }
        }
    }
}

export default services;
