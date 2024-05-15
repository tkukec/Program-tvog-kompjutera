import axios from 'axios';

// Mocking axios
const mockAxios = {
  get: (url) => {
    // Return mock data based on the URL
    if (url === '/api/events') {
      return Promise.resolve({
        data: [
          // Mock event data
          {
            id: 1,
            name: 'Phishing Event 1',
            brand: 'Brand A',
            description: 'Description of phishing event 1',
            url: 'http://malicious-url.com',
            date: '2024-01-01',
            dnsRecords: { A: ['192.168.1.1'], NS: ['ns1.example.com'], MX: ['mail.example.com'] },
            keywords: ['keyword1', 'keyword2'],
            status: 'todo',
            comments: [{ text: 'Initial comment', timestamp: '2024-01-01T12:00:00Z' }]
          }
        ]
      });
    }
    return Promise.reject(new Error('Not found'));
  },
  post: (url, data) => {
    // Handle mock post requests
    if (url === '/api/events') {
      return Promise.resolve({ data: { ...data, id: Date.now() } });
    }
    return Promise.reject(new Error('Error'));
  }
};

export default mockAxios;