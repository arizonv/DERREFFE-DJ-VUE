const BASE_URL = 'http://127.0.0.1:8000/api/';

class ApiUsers {
  async getUser() {
    const response = await fetch(BASE_URL);
    return await response.json();
  }
}

export default new ApiUsers();
