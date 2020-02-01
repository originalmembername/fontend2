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
    <v-img src="https://specials-images.forbesimg.com/imageserve/1026205392/960x0.jpg?fit=scale"></v-img>
    </v-form>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    imgUrl: ""
  }),
  methods: {
    loadImg() {
      // eslint-disable-next-line
      console.log("load image: " + this.imgUrl)
      let imgUrl = this.imgUrl
      axios
          .post("http://127.0.0.1:8000/api/v1/vocabs/imgtest/", {
            imgUrl: imgUrl
          })
          .then(function (resp) {
            //eslint-disable-next-line
            console.log(resp)
            //process the response
          })
    }
  }
}
</script>