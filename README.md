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
      <li>Locate the <code>"pae"</code> key and copy the entire array (including all nested brackets).</li>
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
<p>
The underlying principle is that we want to exclude the self-interaction contribution from the peptides while calculating our interface metric of PAE. Thus, we consider the non-diagonal matrix blocks in the larger matrix defining residue-residue contributions across different peptide chains.

<center>
  <table>
    <tr>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>A</th>
      <td>A→A</td>
      <td>A→B</td>
      <td>A→C</td>
    </tr>
    <tr>
      <th>B</th>
      <td>B→A</td>
      <td>B→B</td>
      <td>B→C</td>
    </tr>
    <tr>
      <th>C</th>
      <td>C→A</td>
      <td>C→B</td>
      <td>C→C</td>
    </tr>
  </table>
</center>
One can similarly visualize for n = 2 or larger cases. The values corresponding to the <code>chain_pair_pae_min</code> key in <code>summay_confidence_n.json</code> would indicate the lowest PAE the model predicts for each pairwise grouping of the different sequences being modeled, to likely achieve in the best case. However, the above iPAE calculations boil down to a single, aggregate, and cumulative measure.
</p>
<p>
iPAE or PAE values could be influenced or biased, such as by small sequence length, but values less than 15 are usually considered. Lastly, the measures are mere approximations for binding affinities, not exact substitutes for them. The various metrics should be used judiciously as they serve different purposes.
</p>
