const routes = [
  {
    name: 'home',
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        name: 'index',
        path: '',
        component: () => import('pages/IndexPage.vue')
      },
      {
        name: 'urls',
        path: 'urls',
        component: () => import('pages/LinksPage.vue')
      },
      {
        name: 'settings',
        path: 'settings',
        component: () => import('pages/SettingsPage.vue')
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
