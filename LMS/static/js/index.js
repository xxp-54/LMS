        function searchBooks() {
            const input = encodeURIComponent(document.getElementById('searchInput').value);
            fetch(`/function.selectBook/`, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' }
            })
            .then(response => response.json())
            .then(data => {
                const resultsTable = document.getElementById('resultsTable');
                const resultsBody = document.getElementById('resultsBody');
                const contentText = document.getElementById('resultDisplay');
                resultsBody.innerHTML = '';
                if (data.results && data.results.length > 0) {
                    contentText.innerText = '';
                    resultsTable.style.display = 'table';
                    data.results.forEach(book => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${book.name}</td>
                            <td>${book.author}</td>
                            <td>
                                <a class="button" href="/delete/${book.id}">借书</a>
                                <a class="button" href="/download/${book.id}">下载</a>
                            </td>
                        ;
                        resultsBody.appendChild(row);
                    });
                } else {
                    contentText.innerText = '未找到相关图书';
                    resultsTable.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('resultDisplay').innerText = '发生错误，请重试。';
            });
        }