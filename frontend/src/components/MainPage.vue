<template>
  <div class="black--text v-card theme--light teal lighten-5">
    <div class="layout" style="height:100%">
      <div class="flex xs3">
        <v-img :src="require('../assets/profile.jpg')" aspect-ratio="2.75" style="height:100%"></v-img>
      </div>
      <div class="flex xs7">
        <div class="v-card__title v-card__title--primary">
          <div>
            <div class="headline">Welcome</div>
            <div>{{texts[0].message}}</div>
            <div><a href="/about">Read more</a></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    texts: [
      {message: "My name is Peter Binder. I've been a language teacher for over 7 years..."}
    ]      
   } )
}
</script>
