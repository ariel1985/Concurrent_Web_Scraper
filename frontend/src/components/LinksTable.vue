<template>
    <q-page class="q-pa-md full-width">
        <q-table
        :rows="data"
        :columns="columns"
        row-key="url"
        :loading-text="loading ? 'Loading data...' : 'No data'"
        />
    </q-page>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

// create variable data as ref to store the data from the API
const data = ref([])
let loading = true

const columns = [
  { name: 'url', label: 'URL', field: 'url', sortable: true }
]

async function fetchData () {
  try {
    if (!import.meta.env.VITE_API_URL) {
      throw new Error('API URL is not defined')
    }
    const url = import.meta.env.VITE_API_URL + '/links'
    const response = await axios.get(url)

    if (!response.data) {
      throw new Error('No data in the response')
    }

    // Map the data to the expected structure
    data.value = response.data.map(item => ({ url: item }))
    loading = false
  } catch (error) {
    console.error(error)
    loading = false
  }
}

fetchData()
</script>
