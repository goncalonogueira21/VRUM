<template> 
  <v-card class="transparent">
    <v-data-table
      class="transparent"
      :headers="headers"
      :items="viagens"
      :page="page"
      :pageCount="numberOfPages"
      :hide-default-footer="true"
      :options.sync="options"
      sort-by="name"
    >

    <template v-slot:item.id="{ item }">
          <div style="cursor: pointer" @click.stop="pushOtherPage">{{ item.id }}</div>
      </template>
      
    </v-data-table>

  </v-card>
</template>

<script>

export default {
  name: "ViagensPorFiltro",
  props:['viagens'],
  data: () => {
    return {
      itemid: 0,
      page: 1,
      totalItems: 0,
      numberOfPages: 0,
      loading: true,
      options: {},
      headers: [
        {
          text: "ID Viagem",
          value: "id",
          sortable: false,
        },
        {
          text: "Condutor",
          value: "condutor",
          sortable: false,
        },
        {
          text: "Carro",
          value: "username",
          sortable: false,
        },
        {
          text: "Origem",
          value: "localInicio",
        },
        {
          text: "Destino",
          value: "localDestino",
        },
        {
          text: "Data",
          value: "dataInicio",
        },
        {
          text: "Hora",
          value: "horaInicial",
        },
        {
          text: "Lugares Disponivel",
          value: "lugaresDisp",
        },
        {
          text: "Bagagem",
          value: "bagagem",
        },
        {
          text: "Custo por Pessoa",
          value:"custoPessoa"
        }
      ],
     
    };
  },
  methods: {
    
    pushOtherPage() {
      this.$router.push({ name: 'Viagem' });
    },
  }
  }
</script>