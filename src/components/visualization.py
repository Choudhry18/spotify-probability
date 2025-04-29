import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import nbinom

def plot_play_distribution(data):
    # Assuming 'data' contains the necessary information for plotting
    r = 1  
    x = np.arange(0, 500)  # Number of failures before first success (0 means first play is the top track)
    pmf = nbinom.pmf(x, 1, data["estimated_probability"])

    # Expected number of plays until hearing top track
    expected_plays = r / data["estimated_probability"]
    print(f"Expected number of plays until hearing the top track: {expected_plays:.2f}")

    # Visualization
    plt.figure(figsize=(10,6))
    plt.bar(x + 1, pmf, alpha=0.7)  # x+1 because we count plays, not failures
    plt.axvline(expected_plays, color='red', linestyle='--', label=f'Expected Plays: {expected_plays:.2f}')
    plt.title('Plays On Shuffle Until Top Track')
    plt.xlabel('Number of Plays')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)

def plot_conditional_probabilities(probabilities):
    labels = ['P(Skip | Prev Skipped)', 'P(Not Skip | Prev Skipped)', 
              'P(Skip | Prev Not Skipped)', 'P(Not Skip | Prev Not Skipped)']
    values = probabilities

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color=['orange', 'green', 'blue', 'purple'], alpha=0.7)
    plt.title('Conditional Probabilities of Skipping Behavior')
    plt.ylabel('Probability')
    plt.ylim(0, 1)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(plt)

def plot_chi_square_results(observed, expected, artist_labels):
    x = np.arange(len(artist_labels))
    plt.figure(figsize=(10, 6))
    plt.bar(x - 0.2, observed, width=0.4, label='Observed', alpha=0.7)
    plt.bar(x + 0.2, expected, width=0.4, label='Expected', alpha=0.7)
    plt.xticks(x, artist_labels, rotation=45, ha='right')
    plt.ylabel('Number of Plays')
    plt.title('Observed vs Expected Plays by Artist')
    plt.legend()
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(plt)