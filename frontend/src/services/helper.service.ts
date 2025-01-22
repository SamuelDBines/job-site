import axios from "axios";

const getApiUrl = (url: string) => `/api/${url}`;

const getAuthorization = () => ({ Authorization: localStorage.getItem('token') });
export const post = (url: string, data: object) => axios.post(getApiUrl(url), data, {
  headers: {
    ...getAuthorization()
  }
});

export const get = (url: string) => axios.get(getApiUrl(url), {
  headers: {
    ...getAuthorization()
  }
});
