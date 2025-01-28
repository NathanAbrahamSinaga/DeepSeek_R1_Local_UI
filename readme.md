# Local Deepseek R1 User Interface

## Instalasi

1. **Instal Ollama**:
   - Unduh dan instal Ollama dari [situs resmi](https://ollama.com/library/deepseek-r1).
   - Jalankan Ollama
     ```bash
     ollama run deepseek-r1:1.5b
     ```

2. **Clone**:
   - Clone repository ini:
     ```bash
     git clone https://github.com/NathanAbrahamSinaga/DeepSeek_R1_Local_UI.git
     cd DeepSeek_R1_Local_UI
     ```
     
3. **Instal Dependensi**:
   - Pastikan Python 3.8+ terinstal.
   - Instal dependensi:
     ```bash
     pip install streamlit langchain-ollama langchain-core
     ```

4. **Jalankan Program**
    ```bash
    streamlit run main.py
    ```

4. **Buka**:
   - Buka browser dan akses `http://localhost:8501`.
