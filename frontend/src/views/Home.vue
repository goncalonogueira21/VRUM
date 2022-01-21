<template>
  <v-container>
    <v-card class="d-flex justify-center mb-6" flat>
      <img src="../assets/VRUM_logo.png" />
    </v-card>
    <v-card class="d-flex justify-center mb-6" flat>
      <v-btn to="/auth" color="#7e380e" class="white--text"> Entrar </v-btn>
    </v-card>
    <v-card class="center">
      <h1>My coords</h1>
      <p>{{ coordinates.lat }} : {{ coordinates.lng }}</p>
    </v-card>
    <v-card class="center">
      <v-text-field
        color="#7e380e"
        label="Localização"
        v-model="local"
      ></v-text-field>
    </v-card>
    <GmapMap
      :center="coordinates"
      :zoom="zoom"
      style="width: 640px; height: 360px; margin: 32px auto"
      ref="mapRed"
      @dragend="handleDrag"
    ></GmapMap>
  </v-container>
</template>

<script>
export default {
  name: "Home",

  data() {
    return {
      coordinates: {
        lat: 41.558364,
        lng: -8.397838,
      },
      local: "Vieira do Minho",
      zoom: 16,
    };
  },

  created() {
    console.log("ENTROU");
    if (localStorage.center) {
      this.coordinates = JSON.parse(localStorage.center);
    }
    if (localStorage.zoom) {
      this.coordinates = parseInt(localStorage.zoom);
    }
  },

  mounted() {
    // add the mao to a data object
    this.$refs.mapRef.$mapPromise.then((map) => (this.map = map));
  },

  computed: {
    currentRouteName() {
      console.log(this.$route.name);
      return this.$route.name;
    },

    mapCoordinates() {
      if (!this.map) {
        return {
          lat: 41.558364,
          lng: -8.397838,
        };
      }
      return {
        lat: this.map.getCenter().lat(),
        lng: this.map.getCenter().lng(),
      };
    },
  },

  methods: {
    handleDrag() {
      // get center and zoom level, store in localstore
      let center = {
        lat: this.map.getCenter().lat(),
        lng: this.map.getCenter().lng(),
      };
      let zoom = this.map.getZoom();

      localStorage.center = JSON.stringify(center);
      localStorage.zoom = zoom;
    },
  },
};
</script>

<style>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
</style>
