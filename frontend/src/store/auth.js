import axios from "axios"

export default {
    namespaced: true,
    state:{
        token: localStorage.getItem('user-token') || '',
        user:   localStorage.getItem('user-email') || '',
    },
    mutations:{
        SET_TOKEN (state,token){
            state.token=token
        },
        SET_USER(state,mail){
            state.user=mail
        },
        USER_LOGOUT(state){
            state.token=''
            state.user=''
        }
    },
    actions:{
        async signIn({ commit }, credentials) {
            try{
                let response = await axios.post("http://localhost:5000/utilizador/login",credentials,{
                headers: { 'Content-Type': 'application/json' } 
                })
            commit('SET_TOKEN', response.data.token)
            commit('SET_USER',credentials.email)
            localStorage.setItem('user-token', response.data.token)
            localStorage.setItem('user-email', credentials.email)
            return response;
            } catch(error) {
                localStorage.removeItem('user-token')
                return error.response;
            }
        },
        logOut({commit}){
            commit('USER_LOGOUT')
            localStorage.removeItem('user-token')
            localStorage.removeItem('user-email')
        }
    },
    getters: {
        isAuthenticated: state => !!state.token,  
    }
}