<template>
    <v-form>
      <h1>Search image</h1>
    <v-container>
      <v-row name="row1">

        <v-col name="col1" cols="12" sm="6" md="3">
          <v-text-field
            label="Regular"
            v-model="imgUrl"
          ></v-text-field>
          <v-btn @click="loadImg">Load Image</v-btn>
        </v-col>
      </v-row>
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