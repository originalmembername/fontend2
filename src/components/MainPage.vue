<template>
  <div>
    <div class="black--text v-card theme--blue-grey lighten-5" style="height:400px">
      <div class="layout">
        <div class="flex xs5">
          <div class="v-responsive v-image" style="height: 125px;">
            <div class="v-responsive__sizer" style="padding-bottom: 100%;"></div>
            <div class="v-image__image v-image__image--contain">
              <v-img src="require(/assets/profile.jpg)" aspect-ratio="2.75"></v-img>
            </div>
            <div class="v-responsive__content"></div>
          </div>
        </div>
        <div class="flex xs7">
          <div class="v-card__title v-card__title--primary">
            <div>
              <div class="headline">Supermodel</div>
              <div>Foster the People</div>
              <div>(2014)</div>
            </div>
          </div>
        </div>
      </div>
      <hr class="v-divider theme--light">
      <div class="v-card__actions pa-3">
        Rate this album
        <div class="spacer"></div>
        <i aria-hidden="true" class="v-icon material-icons theme--light">star_border</i>
        <i aria-hidden="true" class="v-icon material-icons theme--light">star_border</i>
        <i aria-hidden="true" class="v-icon material-icons theme--light">star_border</i>
        <i aria-hidden="true" class="v-icon material-icons theme--light">star_border</i>
        <i aria-hidden="true" class="v-icon material-icons theme--light">star_border</i>
      </div>
    </div>
  </div>
</template>
