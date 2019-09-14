<template>
  <v-flex style="overflow:scroll; max-height: 70vh">
    <v-card v-for="vocab in vocabsObj._data.vocabList" :key="vocab.german">
        <v-layout row>
          <label class="form-checkbox">
            <input
              align-center
              justify-center
              type="checkbox"
              :value="vocab.german"
              v-model="vocabsObj._data.selected"
            />
            <i class="form-icon"></i>
          </label>
          <v-img
            @click="edit(vocab)"
            :src="getImage(vocab)"
            class="thumbnail"
            :contain = "true"
            max-height="80px"

          ></v-img>
          <v-layout column>
            <v-card-text :label="vocab.german">
              <h3>{{vocab.german}}</h3>
              <h5>{{vocab.english}}</h5>
            </v-card-text>
          </v-layout>
        </v-layout>
    </v-card>
  </v-flex>
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