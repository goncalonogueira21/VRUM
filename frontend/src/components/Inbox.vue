<template>
<v-container
          class="fill-height pa-0 "
        >
          <v-row class="no-gutters elevation-4">
            <v-col
              cols="12" sm="3"
              class="flex-grow-1 flex-shrink-0"
              style="border-right: 1px solid #0000001f;"
            >
              <v-responsive v-if="activeChat==0"
                class="overflow-y-auto fill-height"
                height="500"
              >
                <v-list subheader>
                  <v-list-item-group 
                      v-model="activeChat"
                      active-class="brown--text"
                    >
                    <template v-for="(item, index) in parents">
                      <v-list-item
                        :key="`parent${index}`"
                        :value="item.id"
                      >
                        <v-list-item-avatar>
                           <v-img
                              class="rounded-circle elevation-8 d-inline-block"
                              src="https://demos.creative-tim.com/vue-material-dashboard/img/marc.aba54d65.jpg"
                              width="128"
                            />
                        </v-list-item-avatar>

                        

                        <v-list-item-content>
                          <v-list-item-title v-text="item.title" />
                        </v-list-item-content>


                      </v-list-item>
                      <v-divider
                        :key="`chatDivider${index}`"
                        class="my-0"
                      />
                    </template>
                  </v-list-item-group>
                </v-list>
              </v-responsive>
            </v-col>
            <v-col
              cols="auto"
              class="flex-grow-1 flex-shrink-0"
            >
              <v-responsive
                v-if="activeChat"
                class="overflow-y-hidden fill-height"
                height="500"
              >
                <v-card
                  flat
                  class="d-flex flex-column fill-height"
                >
                  <v-card-title>
                    <v-icon class="mr-4" color="#7e380e" @click="activeChat=0"> mdi-arrow-left </v-icon>
                    {{(parents[activeChat-1]).title}}
                  </v-card-title>
                  <v-card-text class="flex-grow-1 overflow-y-auto">
                    <template v-for="msg in messages" >
                      <div
                        :class="{ 'd-flex flex-row-reverse': msg.me }"
                        :key="msg.id"
                      >
                        <v-menu offset-y>
                          <template v-slot:activator="{ on }">
                            <v-hover
                              v-slot:default="{ hover }"
                            >
                              <v-chip
                                :color="msg.me ? '#7e380e' : ''"
                                dark
                                style="height:auto;white-space: normal;"
                                class="pa-4 mb-2"
                                v-on="on"
                              >
                                {{ msg.content }}
                                <sub
                                  class="ml-2"
                                  style="font-size: 0.5rem;"
                                >{{ msg.created_at }}</sub>
                                <v-icon
                                  v-if="hover"
                                  small
                                >
                                  expand_more
                                </v-icon>
                              </v-chip>
                            </v-hover>
                          </template>
                          <v-list>
                            <v-list-item>
                              <v-list-item-title>delete</v-list-item-title>
                            </v-list-item>
                          </v-list>
                        </v-menu>
                      </div>
                    </template>
                  </v-card-text>
                  <v-card-text class="flex-shrink-1">
                      <v-text-field
                      color="#7e380e"
                      v-model="content"
                      label="Escreva a sua mensagem"
                      type="text"
                      no-details
                      outlined
                      append-outer-icon="mdi-send"
                      @keyup.enter="sendMessage((parents[activeChat-1]).title)"
                      @click:append-outer="sendMessage((parents[activeChat-1]).title)"
                      hide-details
                    />
                  </v-card-text>
                </v-card>
              </v-responsive>
            </v-col>
          </v-row>
    </v-container>
</template>

<script>
import { mapState } from "vuex";
  export default {
     computed: mapState({
    username: (state) => state.auth.username
  }),
    data: () => ({
        //no mounted é suposto carregar para aqui as mensagens de um user bem com o avatar da pessoa e o nome dela
      activeChat: 0,
    parents: [],
    messages: [],
    content:"",
    created_at:""
    }),
    watch:{
      activeChat: function(newval){
        if(newval!=0){
          this.enterChat(this.parents[newval-1].title)
        }
      }
    },
    created(){
        var now     = new Date(); 
        var year    = now.getFullYear();
        var month   = now.getMonth()+1; 
        var day     = now.getDate();
        var hour    = now.getHours();
        var minute  = now.getMinutes();
        var second  = now.getSeconds(); 
        if(month.toString().length == 1) {
             month = '0'+month;
        }
        if(day.toString().length == 1) {
             day = '0'+day;
        }   
        if(hour.toString().length == 1) {
             hour = '0'+hour;
        }
        if(minute.toString().length == 1) {
             minute = '0'+minute;
        }
        if(second.toString().length == 1) {
             second = '0'+second;
        }   
        var dateTime = year+'/'+month+'/'+day+' '+hour+':'+minute+':'+second;   
         
    

    this.created_at = dateTime;
    this.$request("get","mensagem/mailbox/" + this.username)
      .then((response)=>{
        //console.log(response.data.Mailbox)
        this.parents=response.data.Mailbox
      }).catch((error)=>{
        console.log(error)
      })
    },
    methods:{
      sendMessage(userDestino){
        const messageForm ={
            content: this.content,
            me: true,
            created_at: this.created_at
        }
        
        var payload = new FormData();
        payload.append('content', messageForm.content);
        payload.append('userOrigem', this.username);
        payload.append('userDestino', userDestino);
        payload.append('created_at', messageForm.created_at)
        this.$request("post","mensagem/registo", payload)
          .then((response)=>{
            console.log(response)
            this.messages.push(messageForm)
          }).catch((error)=>{
            console.log(error)
          })
        this.content=''
      },
      enterChat(userDestino){
        this.$request("get","mensagem/" + this.username + "&" + userDestino)
          .then((response)=>{
            console.log("mensagens :"+response.data.Mensagens)
            this.messages=response.data.Mensagens
          }).catch((error)=>{
            console.log(error)
          })
          }
    } 
}
</script>