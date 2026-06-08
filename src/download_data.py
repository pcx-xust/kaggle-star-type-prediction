import kagglehub

def main():
    path = kagglehub.competition_download("playground-series-s6e6")
    print(f"Competition files downloaded to: {path}")
  
if __name__ == "__main__":
    main()
