<template>
    <v-form>
      <h1>Search image</h1>
    <v-container>
      <v-layout column>
        <v-flex xs6>
          <v-text-field
            label="URL"
            v-model="imgUrl"
          ></v-text-field>
        </v-flex>
        <v-flex xs6>
          <v-text-field
            label="German"
            v-model="german"
          ></v-text-field>
        </v-flex>
        <v-flex xs6>
          <v-text-field
            label="English"
            v-model="english"
          ></v-text-field>          
        </v-flex>
        <v-btn @click="loadImg">Load Image</v-btn>
      </v-layout>
    </v-container>
    <v-img :src="imgSrc" alt="the image"></v-img>
    </v-form>
</template>

<script>
/* eslint-disable */
import axios from 'axios'

export default {
  data: () => ({
    imgUrl: "",
    german: "",
    english: "",
    imgSrc: "https://image.shutterstock.com/image-vector/picture-vector-icon-no-image-260nw-1350441335.jpg"
  }),
  methods: {
    loadImg() {
      // eslint-disable-next-line
      console.log("load image: " + this.imgUrl)
      let imgUrl = this.imgUrl
      let german = this.german
      let english = this.english
      let setImgSrc = this.setImgSrc
      axios
          .post("http://127.0.0.1:8000/api/v1/vocabs/imgtest/", {
            imgUrl: imgUrl,
            german: german,
            english: english
          })
          .then(function (resp) {
            //eslint-disable-next-line
            console.log(resp)
            setImgSrc(resp.data.image)
            //process the response
          })
    },
    setImgSrc(src){
      this.imgSrc = src
    }    
  }
}
</script>