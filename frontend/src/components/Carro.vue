<template>
  <v-data-table
    :headers="headers"
    :items="carros"
    :search="search"
    sort-by="matricula"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="800px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="#7e380e"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
              @click="formTitle()"
            >
              ADICIONAR CARRO
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle1 }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      :rules="[rules.required]"
                      required
                      color="#7e380e"
                      v-model="editedItem.matricula"
                      label="Matrícula"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      :rules="[rules.required]"
                      required
                      color="#7e380e"
                      v-model="editedItem.marca"
                      label="Marca"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      :rules="[rules.required]"
                      required
                      color="#7e380e"
                      v-model="editedItem.modelo"
                      label="Modelo"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      :rules="[rules.required]"
                      required
                      color="#7e380e"
                      v-model="editedItem.ano"
                      label="Ano"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      :rules="[rules.required]"
                      required
                      color="#7e380e"
                      v-model="editedItem.cor"
                      label="Cor"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      :rules="[rules.required]"
                      required
                      color="#7e380e"
                      v-model="editedItem.lugares"
                      label="Lugares disponíveis"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      :rules="[rules.required]"
                      required
                      color="#7e380e"
                      v-model="editedItem.combustivel"
                      label="Tipo de combustível"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    
                  >
                    <label class="text-h6 mb-2 text--secondary">
                        Inserir fotografia do carro  
                        </label>
                    <input class="text-h7 mb-2 text--secondary"  type="file" accept="image/*" @change="handleFileUpload( $event )"/>
                    
                </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="#7e380e"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="#7e380e"
                text
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title color="#7e380e" class="text-h5">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="#7e380e" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="#7e380e" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.foto="{ item }">
          <img :src="item.foto" style="width: 50px; height: 50px" />
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        color="#7e380e"
        small
        class="mr-2"
        @click="editItem(item), formTitle()"
      >
        mdi-pencil
      </v-icon> 
      <v-icon
        color="#7e380e"
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import {mapState} from "vuex"

  export default {
    data: () => ({
      dialog: false,
      dialogDelete: false,
      search:"",
      headers: [
        {
          text: 'Matrícula',
          align: 'start',
          sortable: false,
          value: 'matricula',
        },
        { text: 'Marca', value: 'marca' },
        { text: 'Modelo', value: 'modelo' },
        { text: 'Ano', value: 'ano' },
        { text: 'Cor', value: 'cor' },
        { text: 'Lugares', value: 'lugares' },
        { text: 'Combustivel', value: 'combustivel'},
        { text: 'Foto', value: 'foto'},
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      carros: [],
      editedIndex: -1,
      editedItem: {
        matricula: '',
        marca: '',
        modelo: '',
        ano: '',
        cor: '',
        lugares: '',
        combustivel: '',
        foto:'',
      },
      defaultItem: {
        matricula: '',
        marca: '',
        modelo: '',
        ano: '',
        cor: '',
        lugares: '',
        combustivel: '',
        foto:'',
      },
      formTitle1:'',
      rules: {
      required: value => !!value || "Required.",
      },
      file:''
    }),

    computed: 
      mapState({
        username: state => state.auth.username
        }),
        
      
    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.initialize()
    },

    methods: {
      formTitle () {
        return this.editedIndex === -1 ? this.formTitle1='Novo Carro' : this.formTitle1='Editar Carro'
      },

      initialize () {
          this.$request("get","carro/" + this.username)
              .then((response)=>{
                this.carros=response.data.Carros
              }).catch((error)=>{
                console.log(error)
              })
      },

      editItem (item) {

        this.editedIndex = this.carros.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.carros.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.$request("delete","carro/" + this.editedItem.matricula + "/remove")
          .then((response)=>{
            console.log(response)
          }).catch((error)=>{
            console.log(error)
          })

        this.carros.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        var payload = new FormData();
        payload.append('matricula', this.editedItem.matricula);
        payload.append('fk_Utilizador_username', this.username );
        payload.append('modelo',this.editedItem.modelo );
        payload.append('tipoFuel', this.editedItem.combustivel);
        payload.append('cor',this.editedItem.cor );
        payload.append('lugares',this.editedItem.lugares );
        payload.append('ano', this.editedItem.ano);
        payload.append('foto', this.file);
        payload.append('marca', this.editedItem.marca);
        

        if (this.editedIndex > -1) {
          this.$request("put", "carro/" + this.editedItem.matricula + "/update", payload)
          .then((response)=>{
            console.log(response)
          }).catch((error)=>{
            console.log(error)
          })
          
        } else {
          this.$request("post","carro/registo", payload, {'Content-Type': ' multipart/form-data'} )
          .then((response)=>{
            console.log(payload.foto)
              console.log(response)
          })
          .catch((error)=>{
            console.log(error)
          })
          
        }

        if (this.editedIndex > -1) {
          Object.assign(this.carros[this.editedIndex], this.editedItem)
        } else {
          this.carros.push(this.editedItem)
        }
        this.close()
        
      },
      handleFileUpload( event ){
        this.file = event.target.files[0];
        this.editedItem.foto=URL.createObjectURL(this.file)
    }
    }
  }
</script>