<template>
    <v-form>
      <h1>Search image</h1>
    <v-container>
      <v-layout row>
        <v-flex xs6>
          <v-text-field
            label="Regular"
            v-model="imgUrl"
          ></v-text-field>
          <v-btn @click="loadImg">Load Image</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
    </v-form>
</template>

<script>
export default {
  data: () => ({
    imgUrl: ""
  }),
  methods: {
    loadImg() {
      // eslint-disable-next-line
      console.log("load image: " + this.imgUrl)
    }
  }
}
</script>