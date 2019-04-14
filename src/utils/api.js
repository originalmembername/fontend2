const mocks = {
  'auth': { 'POST': { user: 'user1', token: 'This-is-a-mocked-token' } },
  'user/me': { 'GET': { name: 'doggo', title: 'sir' } }
}

const apiCall = ({url, method, ...args}) => new Promise((resolve, reject) => {
  setTimeout(() => {
    try {
      resolve(mocks[url][method || 'GET'])
      console.log(`Mocked '${url}' - ${method || 'GET'}`)
      console.log('response: ', mocks[url][method || 'GET'])
    } catch (err) {
      reject(new Error(err))
    }
  }, 1000)
})

const users = {
  'klaus@gmail.com' : {
    'name' : 'Klaus',
    'password' : 'pwd1'
  },
  'helga@web.de' : {
    'name' : 'helga',
    'password' : 'pwd2'
  }

}

export default apiCall
