class ApiService {
    async getPosts() {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts');
      return await response.json();
    }
  
    async getPost(id) {
      const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
      return await response.json();
    }
    
  
    async addPost(post) {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(post)
      });
      return await response.json();
    }
  
    async updatePost(id, post) {
      const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(post)
      });
      return await response.json();
    }
  
    async deletePost(id) {
      const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
        method: 'DELETE'
      });
      return await response.json();
    }
  }
  
  
export default new ApiService();
  