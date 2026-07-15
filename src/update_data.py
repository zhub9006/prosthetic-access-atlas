#!/usr/bin/env python3
"""
Prosthetic Access Atlas — Data Update Script

This script demonstrates how to programmatically update the atlas with new
ClinicalTrials.gov data and OpenStreetMap provider information.

Requirements:
    pip install requests

Usage:
    python update_data.py
"""

import requests
import json
import time

# ClinicalTrials.gov API
BASE_URL = "https://clinicaltrials.gov/api/v2/studies"

def search_prosthetic_studies(max_results=200):
    """Search for prosthetic studies from ClinicalTrials.gov."""
    params = {
        "query.cond": "prosthesis",
        "pageSize": max_results,
        "fields": "NCTId,BriefTitle,OverallStatus,Condition,LocationCountry",
    }
    studies = []
    page_token = None
    
    while True:
        if page_token:
            params["pageToken"] = page_token
        try:
            resp = requests.get(BASE_URL, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            studies.extend(data.get("studies", []))
            print(f"Retrieved {len(studies)} studies so far...")
            
            # Check for next page
            next_token = data.get("nextPageToken")
            if not next_token:
                break
            page_token = next_token
            time.sleep(1)  # Rate limiting
        except requests.exceptions.RequestException as e:
            print(f"Error fetching studies: {e}")
            break
    
    return studies

def analyze_study_status(studies):
    """Analyze studies by status."""
    status_counts = {}
    for study in studies:
        status = study.get("protocolSection", {}).get("statusModule", {}).get("overallStatus", "UNKNOWN")
        status_counts[status] = status_counts.get(status, 0) + 1
    return status_counts

def analyze_study_phase(studies):
    """Analyze studies by phase."""
    phase_counts = {}
    for study in studies:
        phase = study.get("protocolSection", {}).get("statusModule", {}).get("phase", "Unknown")
        phase_counts[phase] = phase_counts.get(phase, 0) + 1
    return phase_counts

def analyze_study_country(studies):
    """Analyze studies by country."""
    country_counts = {}
    for study in studies:
        locations = study.get("protocolSection", {}).get("contactsLocationsModule", {}).get("locations", [])
        countries = set()
        for loc in locations:
            country = loc.get("country", "Unknown")
            if country:
                countries.add(country)
        for c in countries:
            country_counts[c] = country_counts.get(c, 0) + 1
    return country_counts

def save_json(data, filepath):
    """Save data to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved to {filepath}")

if __name__ == "__main__":
    print("="*60)
    print("Prosthetic Access Atlas — Data Update")
    print("="*60)
    
    # Fetch studies
    print("\n[1/4] Fetching prosthetic studies...")
    studies = search_prosthetic_studies(max_results=200)
    print(f"Retrieved {len(studies)} studies")
    
    # Analyze
    print("\n[2/4] Analyzing by status...")
    status = analyze_study_status(studies)
    save_json(status, "data/status_counts.json")
    
    print("\n[3/4] Analyzing by phase...")
    phase = analyze_study_phase(studies)
    save_json(phase, "data/phase_counts.json")
    
    print("\n[4/4] Analyzing by country...")
    country = analyze_study_country(studies)
    save_json(country, "data/country_counts.json")
    
    # Save full study list
    save_json(studies, "data/all_studies.json")
    
    print("\n" + "="*60)
    print("Update complete!")
    print("="*60)
    
    # Print summary
    print("\nStatus Summary:")
    for s, c in sorted(status.items(), key=lambda x: -x[1]):
        print(f"  {s}: {c}")