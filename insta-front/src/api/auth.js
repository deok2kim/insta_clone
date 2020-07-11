import http from './http';

export async function login(username, password) {
  return http.post( url:'/login', data:{
    username,
    password
  })
}