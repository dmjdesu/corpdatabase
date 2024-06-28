import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import DetailSearchForm from './components/DetailSearchForm';

const App = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [activePopup, setActivePopup] = useState(null);
  const [tagCount, setTagCount] = useState(0);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const showPopup = (type) => {
    setActivePopup(type);
  };

  const closePopup = () => {
    setActivePopup(null);
  };

  const applySelections = (type) => {
    // Implement your logic for applying selections
    closePopup();
  };

  const applyTagSelections = () => {
    // Implement your logic for applying tag selections
    closePopup();
  };

  return (
    <div className="App">
      <header className="header">
        <img src="https://salessystem.co.jp/wpcms/wp-content/uploads/2024/06/SalesDB_logo_by-1.png" alt="SalesDB ロゴ" />
        <div className="menu-toggle" onClick={toggleMenu}>
          <i className="fa-solid fa-bars"></i>
        </div>
        <nav style={{ display: isMenuOpen ? 'block' : 'none' }}>
          <a href="#">SalesDBとは？</a>
          <a href="#">業種から探す</a>
          <a href="#">地域から探す</a>
          <a href="#">#タグから探す</a>
        </nav>
        <div className="button-container">
          <a href="#" className="button">無料会員登録</a>
          <a href="#" className="button">会員ログイン</a>
        </div>
      </header>
      <main className="overlay">
        <h1 className="headline">登録データ数が業界最多の800万件以上<br />国内最大級の企業/店舗/施設データベース</h1>
        <div class="logo-container">
            <img src="https://salessystem.co.jp/wpcms/wp-content/uploads/2024/05/SalesDB_モノトーン_logo_by表記あり_白抜き.png" alt="SalesDB ロゴ" class="logo"/>
        </div>
        <div className="search-results">
          <div className="hexagon">
            <img src="https://salessystem.co.jp/wpcms/wp-content/uploads/2024/06/mark.png" alt="月300件まで無料ダウンロード" />
          </div>
          <div className="search-count">検索結果 <span>8,320,452</span>件</div>
        </div>
        <div className="search-box">
          <input type="text" placeholder="業種" readOnly onClick={() => showPopup('industry')} />
          <input type="text" placeholder="地域" readOnly onClick={() => showPopup('region')} />
          <input type="text" placeholder="フリーワード" />
          <button>検索</button>
        </div>
        <DetailSearchForm />
        <div className="tags">
          <a href="#" className="tag">#店舗</a>
          <a href="#" className="tag">#株式会社のみ</a>
          <a href="#" className="tag">#設立3年以内の企業</a>
          <a href="#" className="tag">#官公庁</a>
          <a href="#" className="tag">#営業お断りをしている企業</a>
          <a href="#" className="tag">#中途採用と新卒採用の両方を行っている企業</a>
        </div>
        <a href="#" className="more-tags">その他のタグから探す <i>&gt;</i></a>
      </main>
      <a href="#" className="cta-button">今すぐフリープランに登録する <i>&gt;</i></a>
      {activePopup === 'industry' && <IndustryPopup onClose={closePopup} applySelections={applySelections} />}
      {activePopup === 'region' && <RegionPopup onClose={closePopup} applySelections={applySelections} />}
      {activePopup === 'tag' && <TagPopup onClose={closePopup} applyTagSelections={applyTagSelections} tagCount={tagCount} />}
    </div>
  );
};

const IndustryPopup = ({ onClose, applySelections }) => {
  const [activeTab, setActiveTab] = useState('simple');
  const [categories, setCategories] = useState([]);
  const [subcategories, setSubcategories] = useState([]);
  const [smallcategories, setSmallcategories] = useState([]);
  const [finecategories, setFinecategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [selectedSubcategory, setSelectedSubcategory] = useState(null);
  const [selectedSmallcategory, setSelectedSmallcategory] = useState(null);
  const [selectedOriginCategory, setSelectedOriginCategory] = useState(null);
  const [selectedOriginSubcategory, setSelectedOriginSubcategory] = useState(null);

  const [originCategories, setOriginCategories] = useState([]);
  const [originSubcategories, setOriginSubcategories] = useState([]);

  useEffect(() => {
    // カテゴリデータの取得
    axios.get('/api/industry_categories/')
      .then(response => setCategories(response.data))
      .catch(error => console.error('Error fetching categories:', error));
  }, []);

  useEffect(() => {
    // オリジナルカテゴリデータの取得
    axios.get('/api/origin_industry_categories/')
      .then(response => setOriginCategories(response.data))
      .catch(error => console.error('Error fetching categories:', error));
  }, []);

  const handleCategoryChange = (categoryId) => {
    setSelectedCategory(categoryId);
    // サブカテゴリデータの取得
    axios.get('/api/industries/', { params: { category_id: categoryId } })
      .then(response => setSubcategories(response.data))
      .catch(error => console.error('Error fetching subcategories:', error));
  };

  const handleOriginCategoryChange = (categoryId) => {
    setSelectedOriginCategory(categoryId);
    // オリジナルサブカテゴリデータの取得
    axios.get('/api/industries/', { params: { category_id: categoryId } })
      .then(response => setOriginSubcategories(response.data))
      .catch(error => console.error('Error fetching subcategories:', error));
  };

  const handleSubcategoryChange = (subcategoryId) => {
    setSelectedSubcategory(subcategoryId);
    // 小カテゴリデータの取得
    axios.get('/api/industry_subcategories/', { params: { subcategory_id: subcategoryId } })
      .then(response => setSmallcategories(response.data))
      .catch(error => console.error('Error fetching smallcategories:', error));
  };

  const handleSmallcategoryChange = (smallcategoryId) => {
    setSelectedSmallcategory(smallcategoryId);
    // 詳分類データの取得
    axios.get('/api/industry_details/', { params: { smallcategory_id: smallcategoryId } })
      .then(response => setFinecategories(response.data))
      .catch(error => console.error('Error fetching finecategories:', error));
  };

  const switchTab = (tab) => {
    setActiveTab(tab);
  };

  return (
    <div className="popup-overlay active" onClick={onClose}>
      <div className="popup active" onClick={(e) => e.stopPropagation()}>
        <div className="popup-header">
          <h2>業種を選択</h2>
          <div className="search-count-popup">検索結果 <span>12,345</span>件</div>
          <button onClick={onClose}>&times;</button>
        </div>
        <div className="tabs">
          <div className={`tab ${activeTab === 'simple' ? 'active' : ''}`} onClick={() => switchTab('simple')}>簡易版で選択（オリジナル業種分類）</div>
          <div className={`tab ${activeTab === 'detailed' ? 'active' : ''}`} onClick={() => switchTab('detailed')}>詳細版で選択（日本標準産業分類）</div>
        </div>
        {activeTab === 'simple' && (
          <div className="industry-popup-content active">
            <input type="text" placeholder="キーワードで探す" className="keyword-search" onChange={(e) => console.log('Search keyword simple', e.target.value)} />
            <div className="columns">
              <div className="column">
                <h3>大分類</h3>
                <ul>
                  {originCategories.map(category => (
                    <li key={category.id}>
                      <input type="checkbox" id={`category${category.id}`} onChange={() => handleOriginCategoryChange(category.id)} />
                      <label htmlFor={`category${category.id}`}>{category.code}.{category.name}</label>
                      <span className="count-box">1,234</span>
                    </li>
                  ))}
                </ul>
              </div>
              <div className="column">
                <h3>中分類</h3>
                <ul>
                  {originSubcategories.map(subcategory => (
                    <li key={subcategory.id}>
                      <input type="checkbox" id={`subcategory${subcategory.id}`} onChange={() => console.log(subcategory.id)} />
                      <label htmlFor={`subcategory${subcategory.id}`}>{subcategory.code}.{subcategory.name}</label>
                      <span className="count-box">567</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        )}
        {activeTab === 'detailed' && (
          <div className="industry-popup-content active">
            <input type="text" placeholder="キーワードで探す" className="keyword-search" onChange={(e) => console.log('Search keyword detailed', e.target.value)} />
            <div className="columns">
              <div className="column">
                <h3>大分類</h3>
                <ul>
                  {categories.map(category => (
                    <li key={category.id}>
                      <input type="checkbox" id={`category${category.id}`} onChange={() => handleCategoryChange(category.id)} />
                      <label htmlFor={`category${category.id}`}>{category.code}.{category.name}</label>
                      <span className="count-box">1,234</span>
                    </li>
                  ))}
                </ul>
              </div>
              <div className="column">
                <h3>中分類</h3>
                <ul>
                  {subcategories.map(subcategory => (
                    <li key={subcategory.id}>
                      <input type="checkbox" id={`subcategory${subcategory.id}`} onChange={() => handleSubcategoryChange(subcategory.id)} />
                      <label htmlFor={`subcategory${subcategory.id}`}>{subcategory.code}.{subcategory.name}</label>
                      <span className="count-box">567</span>
                    </li>
                  ))}
                </ul>
              </div>
              <div className="column">
                <h3>小分類</h3>
                <ul>
                  {smallcategories.map(smallcategory => (
                    <li key={smallcategory.id}>
                      <input type="checkbox" id={`smallcategory${smallcategory.id}`} onChange={() => handleSmallcategoryChange(smallcategory.id)} />
                      <label htmlFor={`smallcategory${smallcategory.id}`}>{smallcategory.code}.{smallcategory.name}</label>
                      <span className="count-box">890</span>
                    </li>
                  ))}
                </ul>
              </div>
              <div className="column">
                <h3>細分類</h3>
                <ul>
                  {finecategories.map(finecategory => (
                    <li key={finecategory.id}>
                      <input type="checkbox" id={`finecategory${finecategory.id}`} />
                      <label htmlFor={`finecategory${finecategory.id}`}>{finecategory.code}.{finecategory.name}</label>
                      <span className="count-box">123</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        )}
        <div className="popup-buttons">
          <button onClick={() => applySelections('industry')}>決定する</button>
        </div>
      </div>
    </div>
  );
};

const RegionPopup = ({ onClose, applySelections }) => {
  return (
    <div className="popup-overlay active" onClick={onClose}>
      <div className="popup active" onClick={(e) => e.stopPropagation()}>
        <div className="popup-header">
          <h2>地域を選択</h2>
          <div className="search-count-popup">検索結果 <span>12,345</span>件</div>
          <button onClick={onClose}>&times;</button>
        </div>
        <input type="text" placeholder="キーワードで探す" className="keyword-search" onChange={(e) => console.log('Search region keyword', e.target.value)} />
        <div className="region-popup-content active">
          <div className="column">
            <h3>都道府県</h3>
            <ul>
              <li><input type="checkbox" id="region1" /> <label htmlFor="region1">北海道</label> <span className="count-box">1,234</span></li>
              <li><input type="checkbox" id="region2" /> <label htmlFor="region2">青森県</label> <span className="count-box">567</span></li>
              <li><input type="checkbox" id="region3" /> <label htmlFor="region3">岩手県</label> <span className="count-box">890</span></li>
            </ul>
          </div>
          <div className="column">
            <h3>市区町村</h3>
            <ul>
              {/* Populate municipalities here */}
            </ul>
          </div>
        </div>
        <div className="popup-buttons">
          <button onClick={() => applySelections('region')}>決定する</button>
        </div>
      </div>
    </div>
  );
};

const TagPopup = ({ onClose, applyTagSelections, tagCount }) => {
  return (
    <div className="popup-overlay active" onClick={onClose}>
      <div className="popup active" onClick={(e) => e.stopPropagation()}>
        <div className="popup-header">
          <h2>#タグを選択</h2>
          <div className="search-count-popup">選択済み <span>{tagCount}</span>件</div>
          <button onClick={onClose}>&times;</button>
        </div>
        <input type="text" placeholder="キーワードで探す" className="keyword-search" onChange={(e) => console.log('Search tag keyword', e.target.value)} />
        <div className="tag-popup-content active">
          <div className="columns">
            <div className="column">
              <h3>大分類</h3>
              <ul>
                <li><input type="checkbox" id="tagCategory1" /> <label htmlFor="tagCategory1">カテゴリー1</label> <span className="count-box">123</span></li>
                <li><input type="checkbox" id="tagCategory2" /> <label htmlFor="tagCategory2">カテゴリー2</label> <span className="count-box">456</span></li>
                <li><input type="checkbox" id="tagCategory3" /> <label htmlFor="tagCategory3">カテゴリー3</label> <span className="count-box">789</span></li>
              </ul>
            </div>
            <div className="column">
              <h3>中分類</h3>
              <ul>
                {/* Populate tag subcategories here */}
              </ul>
            </div>
            <div className="column">
              <h3>小分類</h3>
              <ul>
                {/* Populate tag small categories here */}
              </ul>
            </div>
          </div>
        </div>
        <div className="popup-buttons">
          <button onClick={applyTagSelections}>決定する</button>
        </div>
      </div>
    </div>
  );
};

export default App;
