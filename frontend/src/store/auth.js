import axios from "axios"

export default {
    namespaced: true,
    state:{
        token:null,
        user:null
    },
    mutations:{
        SET_TOKEN (state,token){
            state.token=token
        },
        SET_USER(state,mail){
            state.user=mail
        }
    },
    actions:{
        async signIn({ commit }, credentials) {
            try{
            let response = await axios.post("http://localhost:5000/login",credentials)
            commit('SET_TOKEN', response.data.token)
            commit('SET_USER',credentials.email)
            return response;
            } catch(error) {
               // console.log(error.response)
                return error.response;
            }


        }
    }
}