<template>
  <div id="vocabList">
    <v-card v-for="vocab in vocabsObj._data.vocabList" :key="vocab.german">
      <v-flex xs8>
        <v-layout row>
          <label class="form-checkbox">
            <input
              align-center
              justify-center
              type="checkbox"
              :value="vocab.german"
              v-model="selected"
            />
            <i class="form-icon"></i>
          </label>
          <v-img
            @click="edit(vocab.german, vocab.english)"
            class="thumbnail"
            :src="getImage(vocab)"
            height="100px"
            width="100px"
          ></v-img>
          <v-layout column align-center justify-center>
            <v-card-text :label="vocab.german">
              <h3>{{vocab.german}}</h3>
            </v-card-text>
            <v-card-text :label="vocab.english">
              <h3>{{vocab.english}}</h3>
            </v-card-text>
          </v-layout>
        </v-layout>
      </v-flex>
    </v-card>
  </div>
</template>

<script>
export default {
    data() {
        return {
            vocabsObj: null
        }
    },
    methods : {
        edit(german, english){
            return this.vocabsObj.edit(german, english);
        },
        getImage(vocab){
            return this.vocabsObj.getImage(vocab);
        } 
    }
}
</script>