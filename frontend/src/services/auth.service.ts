import { post } from './helper.service';

export const loginUser = (data: { username: string; password: string; }) => post('token/', data);