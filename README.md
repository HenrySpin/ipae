<h2>How to Use AlphaFold PAE Data in Python</h2>
<ol>
  <li>
    <strong>Run AlphaFold Predictions</strong><br>
    Submit your protein/peptide sequences at <a href="https://alphafoldserver.com" target="_blank">AlphaFold Server</a>.
  </li>
  <li>
    <strong>Download Results</strong><br>
    After completion, download the results ZIP file from the server.
  </li>
  <li>
    <strong>Extract PAE Data</strong><br>
    <ul>
      <li>Open any <code>full_data_n.json</code> file from the results.</li>
      <li>Locate the <code>"pae"</code> key and copy the entire array (including all nested brackets, except the starting and ending bracket).</li>
    </ul>
  </li>
  <li>
    <strong>Paste into Python</strong><br>
    <ul>
      <li>Of the given Python analysis scripts, choose one as per purpose, find the line where the PAE matrix is defined, e.g.:
        <pre><code>pae = np.array([...])</code></pre>
      </li>
      <li>Replace the <code>[...]</code> with the array you copied from the JSON file.</li>
    </ul>
  </li>
  <li>
    <strong>Set Chain Lengths</strong><br>
    <ul>
      <li>Define <code>chain_lengths</code> as a list of amino acid sequence lengths for each peptide/protein chain:
        <pre><code>chain_lengths = [length1, length2, ...]</code></pre>
      </li>
    </ul>
  </li>
</ol>
<p>
  This workflow lets you easily analyze inter-chain PAE values from AlphaFold PAE data for further inference. Interface Predicted Alignment Error, also referred to as iPAE or PAE_i, is used as a surrogate for PPI binding affinities. Thanks to Brian Coventry for showing me the dimeric case. I extended it to cases of trimeric interaction and n peptides for specific utility and generalizability, respectively.
</p>
