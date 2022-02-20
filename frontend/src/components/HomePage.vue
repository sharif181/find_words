<template>
  <div class="container-fluid">
    <!-- Image and text -->
    <MenuSection/>
    <div class="d-flex justify-start">
      <div class="col-7 bg-light m-2">
        <div class="d-flex justify-content-between">
          <div class="m-2">
            <img src="" alt="" style="width: 64px; height: 64px;">
          </div>
          <div class="m-2 mt-2">
            <span v-for="(item, index) in this.text_obj.title" :key="index">
              <span v-if="words.includes(item)"><button @click="showInInfoArea(item)"
                                                        class="btn btn-primary m-1">{{ item }} </button></span>
              <span v-else>{{ item }} </span>
            </span>
          </div>
        </div>
        <div class="mt-2">
          <span v-for="(line, index) in this.text_obj.lines" :key="index">
            <span v-for="(word, w_index) in line" :key="w_index">
              <span v-if="words.includes(word)"><button @click="showInInfoArea(word)"
                                                        class="btn btn-primary m-1">{{ word }} </button></span>
              <span v-else>{{ word }} </span>
            </span>
          </span>
        </div>
      </div>
      <div class="col-5 bg-light m-2">
        <div class="card">
          <div class="card-header">
            <b>selected word: {{ this.selected_word[0] }}</b>
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">
              meaning: <span v-if="selected_word[1] !=='' ">{{ this.selected_word[1] }}</span>
              <span v-else>No data</span>
            </li>
            <li class="list-group-item">
              related words: <span v-if="selected_word[2] !=='' ">{{ this.selected_word[2] }}</span>
              <span v-else>No data</span>
            </li>
            <li class="list-group-item">
              related phrases: <span v-if="selected_word[3] !=='' ">{{ this.selected_word[3] }}</span>
              <span v-else>No data</span>
            </li>
          </ul>
          <button class="btn btn-primary">Button</button>
        </div>
      </div>
    </div>
    <FooterSection/>
  </div>
</template>

<script>
import axios from 'axios'
import FooterSection from "./FooterSection";
import MenuSection from "./MenuSection";

export default {
  name: "HomePage",
  components: {
    FooterSection,
    MenuSection
  },
  data() {
    return {
      text_obj: {},
      word_data: {},
      words: [],
      selected_word: {}
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    async getData() {
      await axios.get(`http://127.0.0.1:8000/api/`)
          .then(res => {
            this.text_obj = res.data.text_obj
            this.word_data = res.data.word_data
            this.words = res.data.words
          })
          .catch()
    },
    showInInfoArea(word) {
      this.selected_word = this.word_data[word]
      console.log(this.selected_word)
    }
  }
}
</script>
