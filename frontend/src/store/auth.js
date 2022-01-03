import axios from "axios"

export default {
    namespaced: true,
    state:{
        token: localStorage.getItem('user-token') || '',
        username:   localStorage.getItem('username') || '',
    },
    mutations:{
        SET_TOKEN (state,token){
            state.token=token
        },
        SET_USER(state,username){
            state.username=username
        },
        USER_LOGOUT(state){
            state.token=''
            state.username=''
        }
    },
    actions:{
        async signIn({ commit }, credentials) {
            try{
                let response = await axios.post("http://localhost:5000/utilizador/login",credentials,{
                headers: { 'Content-Type': 'application/json' } 
                })
            commit('SET_TOKEN', response.data.token)
            commit('SET_USER',credentials.username)
            localStorage.setItem('user-token', response.data.token)
            localStorage.setItem('username', credentials.username)
            return response;
            } catch(error) {
                localStorage.removeItem('user-token')
                return error.response;
            }
        },
        logOut({commit}){
            commit('USER_LOGOUT')
            localStorage.removeItem('user-token')
            localStorage.removeItem('username')
        }
    },
    getters: {
        isAuthenticated: state => !!state.token,  
    }
}