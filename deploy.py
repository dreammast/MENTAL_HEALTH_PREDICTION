#!/usr/bin/env python3
"""
Campus Mind Deployment Script
Automates deployment to various platforms
"""

import os
import subprocess
import sys

def check_requirements():
    """Check if required tools are installed"""
    print("🔍 Checking requirements...")
    
    # Check if git is installed
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
        print("✅ Git is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not installed. Please install Git first.")
        return False
    
    return True

def setup_git():
    """Initialize git repository if not already done"""
    print("📁 Setting up Git repository...")
    
    try:
        # Check if already a git repo
        subprocess.run(['git', 'status'], check=True, capture_output=True)
        print("✅ Git repository already initialized")
    except subprocess.CalledProcessError:
        # Initialize git repo
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)
        print("✅ Git repository initialized")

def deploy_heroku():
    """Deploy to Heroku"""
    print("🚀 Deploying to Heroku...")
    
    try:
        # Check if Heroku CLI is installed
        subprocess.run(['heroku', '--version'], check=True, capture_output=True)
        
        # Get app name from user
        app_name = input("Enter your Heroku app name (or press Enter for 'campus-mind-chatbot'): ").strip()
        if not app_name:
            app_name = "campus-mind-chatbot"
        
        # Create Heroku app
        try:
            subprocess.run(['heroku', 'create', app_name], check=True)
            print(f"✅ Heroku app '{app_name}' created")
        except subprocess.CalledProcessError:
            print(f"ℹ️  App '{app_name}' might already exist")
        
        # Set environment variables
        groq_key = input("Enter your Groq API key: ").strip()
        if groq_key:
            subprocess.run(['heroku', 'config:set', f'GROQ_API_KEY={groq_key}'], check=True)
            print("✅ Environment variables set")
        
        # Deploy
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Deploy to Heroku'], check=True)
        subprocess.run(['git', 'push', 'heroku', 'main'], check=True)
        
        print("✅ Deployment successful!")
        print(f"🌐 Your app is available at: https://{app_name}.herokuapp.com")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Heroku deployment failed: {e}")
    except FileNotFoundError:
        print("❌ Heroku CLI not found. Please install it from https://devcenter.heroku.com/articles/heroku-cli")

def deploy_railway():
    """Deploy to Railway"""
    print("🚀 Deploying to Railway...")
    print("📋 Railway deployment steps:")
    print("1. Go to https://railway.app")
    print("2. Sign in with GitHub")
    print("3. Click 'New Project'")
    print("4. Select 'Deploy from GitHub repo'")
    print("5. Choose this repository")
    print("6. Set environment variable GROQ_API_KEY")
    print("7. Railway will automatically deploy your app")
    print("✅ Follow these steps to complete Railway deployment")

def deploy_render():
    """Deploy to Render"""
    print("🚀 Deploying to Render...")
    print("📋 Render deployment steps:")
    print("1. Go to https://render.com")
    print("2. Sign in with GitHub")
    print("3. Click 'New +' and select 'Web Service'")
    print("4. Connect your GitHub repository")
    print("5. Configure:")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: gunicorn app:app --bind 0.0.0.0:$PORT")
    print("6. Set environment variable GROQ_API_KEY")
    print("7. Click 'Create Web Service'")
    print("✅ Follow these steps to complete Render deployment")

def main():
    print("🎓 Campus Mind Deployment Script")
    print("=" * 40)
    
    if not check_requirements():
        sys.exit(1)
    
    setup_git()
    
    print("\nChoose deployment platform:")
    print("1. Heroku (Recommended)")
    print("2. Railway")
    print("3. Render")
    print("4. Show all options")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        deploy_heroku()
    elif choice == "2":
        deploy_railway()
    elif choice == "3":
        deploy_render()
    elif choice == "4":
        print("\n📋 All deployment options:")
        print("\n🔵 Heroku (Easiest):")
        deploy_heroku()
        print("\n🟡 Railway:")
        deploy_railway()
        print("\n🟢 Render:")
        deploy_render()
    else:
        print("❌ Invalid choice. Please run the script again.")

if __name__ == "__main__":
    main()
