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
                      v-model="messageForm.content"
                      label="Escreva a sua mensagem"
                      type="text"
                      no-details
                      outlined
                      append-outer-icon="mdi-send"
                      @keyup.enter="sendMessage(messageForm)"
                      @click:append-outer="sendMessage(messageForm)"
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
  export default {
    data: () => ({
        //no mounted é suposto carregar para aqui as mensagens de um user bem com o avatar da pessoa e o nome dela
      activeChat: 0,
    parents: [
      {
        id: 1,
        title: "john doe",
        active: true
      },
      {
        id: 2,
        title: "scarlett",
        active: false
      },
      {
        id: 3,
        title: "zat",
        active: false
      },
      {
        id: 4,
        title: "joao",
        active: false
      },
      {
        id: 5,
        title: "edu",
        active: false
      },
      {
        id: 6,
        title: "carlos",
        active: false
      }
    ],
    messages: [
      {
        content: "lorem ipsum",
        me: true,
        created_at: "11:11am"
      },
      {
        content: "dolor",
        me: false,
        created_at: "11:11am"
      },
      {
        content: "dolor",
        me: false,
        created_at: "11:11am"
      },
      {
        content: "dolor",
        me: false,
        created_at: "11:11am"
      },
      {
        content: "dolor",
        me: true,
        created_at: "11:11am"
      },
      {
        content: "dolor",
        me: false,
        created_at: "11:12am"
      },
      {
        content: "dolor",
        me: false,
        created_at: "11:14am"
      }
    ],
    messageForm: {
      content: "",
      me: true,
      created_at: "11:11am"
    }
    }),
    methods:{
      openMessageDialog(userDestino){
          console.log(userDestino)
      },
      sendMessage(msg){
        this.messages.push(msg)
        this.messageForm.content=''
      }
    } 
}
</script>