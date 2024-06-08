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

const columns = [
  { name: 'url', label: 'URL', field: 'url', sortable: true },
  { name: 'scraped_at', label: 'Scraped At', field: 'scraped_at', sortable: true },
  { name: 'datatype', label: 'Data Type', field: 'datatype', sortable: true },
  { name: 'data', label: 'Data', field: 'data', sortable: true }
]

let loading = true

async function fetchData () {
  try {
    if (!import.meta.env.VITE_API_URL) {
      throw new Error('API URL is not defined')
    }
    console.log('url:', import.meta.env.VITE_API_URL)

    const response = await axios.get(import.meta.env.VITE_API_URL)

    if (!response.data) {
      throw new Error('No data in the response')
    }

    console.log('response:')
    console.log(response)
    data.value = response.data
  } catch (error) {
    console.error('Error fetching data:', error.message)
  } finally {
    loading = false
  }
}

fetchData()
</script>
