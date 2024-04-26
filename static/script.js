const ApiUrl = 'http://127.0.0.1:8000/recent/';

async function requestRecent(){
  const response = await fetch(ApiUrl);
  const data = await response.json();
  console.log(data);
  return data;
}
