import React, { useState } from 'react';

const DetailSearchForm = ({ showPopup }) => {
    const [isExpanded, setIsExpanded] = useState(false);

    const clearInputs = (section) => {
        const sectionElement = document.querySelectorAll(`.${section} input, .${section} textarea`);
        console.log("sectionElement")
        console.log(sectionElement)
        sectionElement.forEach(element => {
            if (element.type === 'checkbox') {
                element.checked = false;
            } else {
                element.value = '';
            }
        });
        console.log(`Clear inputs in ${section}`);
    };

    const formatNumber = (input) => {
        const value = input.value.replace(/\D/g, '');
        input.value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    };

    const toggleDetails = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <div style={{ textAlign: 'center' }}>
            <div className="toggle-link" onClick={toggleDetails}>
                詳細検索 <span>{isExpanded ? '\u25B2' : '\u25BC'}</span>
            </div>
            {isExpanded && (
                <div className="details-container">
                    <div className="details">
                        <h3 className="keyword-section">
                            キーワード
                            <button className="clear-button" onClick={() => clearInputs('keyword-section')}>クリア <i className="fas fa-chevron-down"></i></button>
                        </h3>
                        <div className="keyword-section row">
                            <label htmlFor="excludeKeywords">除外するキーワード</label>
                            <textarea id="excludeKeywords" rows="2" placeholder="複数行入力欄"></textarea>
                            <label htmlFor="tags">#タグを選択</label>
                            <input type="text" id="tags" onClick={(e) => showPopup('tag')} readOnly />
                        </div>
                        {/* 他の詳細検索項目 */}
                        <h3 className="performance-section">
                            業績
                            <button className="clear-button" onClick={() => clearInputs('performance-section')}>クリア <i className="fas fa-chevron-down"></i></button>
                        </h3>
                        <div className="performance-section row">
                            <label htmlFor="revenueMin">売上高(年商)</label>
                            <input type="text" id="revenueMin" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>円 ～</span>
                            <input type="text" id="revenueMax" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>円</span>
                        </div>
                        <div className="performance-section row">
                            <label htmlFor="profitMin">経常利益</label>
                            <input type="text" id="profitMin" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>円 ～</span>
                            <input type="text" id="profitMax" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>円</span>
                        </div>
                        <h3 className="scale-section">
                            規模
                            <button className="clear-button" onClick={() => clearInputs('scale-section')}>クリア <i className="fas fa-chevron-down"></i></button>
                        </h3>
                        <div className="scale-section row">
                            <label htmlFor="capitalMin">資本金</label>
                            <input type="text" id="capitalMin" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>円 ～</span>
                            <input type="text" id="capitalMax" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>円</span>
                        </div>
                        <div className="scale-section row">
                            <label htmlFor="establishedYearMin">設立年</label>
                            <input type="text" id="establishedYearMin" className="numeric-only" maxLength="4" onInput={(e) => formatNumber(e.target)} />
                            <span>年 ～</span>
                            <input type="text" id="establishedYearMax" className="numeric-only" maxLength="4" onInput={(e) => formatNumber(e.target)} />
                            <span>年</span>
                        </div>
                        <div className="scale-section row">
                            <label htmlFor="employeesMin">従業員数</label>
                            <input type="text" id="employeesMin" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>人 ～</span>
                            <input type="text" id="employeesMax" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>人</span>
                        </div>
                        <div className="scale-section row">
                            <label htmlFor="branchesMin">事業所数</label>
                            <input type="text" id="branchesMin" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>拠点 ～</span>
                            <input type="text" id="branchesMax" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>拠点</span>
                        </div>
                        <div className="scale-section row">
                            <label htmlFor="storesMin">店舗数</label>
                            <input type="text" id="storesMin" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>店舗 ～</span>
                            <input type="text" id="storesMax" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>店舗</span>
                        </div>
                        <div className="scale-section row">
                            <label htmlFor="factoriesMin">工場数</label>
                            <input type="text" id="factoriesMin" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>箇所 ～</span>
                            <input type="text" id="factoriesMax" className="numeric-only" onInput={(e) => formatNumber(e.target)} />
                            <span>箇所</span>
                        </div>
                        <h3 className="businessType-section">
                            業態
                            <button className="clear-button" onClick={() => clearInputs('businessType-section')}>クリア <i className="fas fa-chevron-down"></i></button>
                        </h3>
                        <div className="businessType-section">
                            <input type="checkbox" id="btob" />
                            <label htmlFor="btob">BtoB</label>
                            <input type="checkbox" id="btoc" />
                            <label htmlFor="btoc">BtoC</label>
                            <input type="checkbox" id="ctoc" />
                            <label htmlFor="ctoc">CtoC</label>
                        </div>
                        <p className="note">※業種指定よりも、こちらの指定が優先されます</p>
                        <h3>
                            連絡先
                            <button className="clear-button" onClick={() => clearInputs('contacts')}>クリア <i className="fas fa-chevron-down"></i></button>
                        </h3>
                        <div className="contacts">
                            <div>
                                <input type="checkbox" id="summary" />
                                <label htmlFor="summary">概要説明が必須</label>
                            </div>
                            <div>
                                <input type="checkbox" id="corporateNumber" />
                                <label htmlFor="corporateNumber">法人番号が必須</label>
                            </div>
                            <div>
                                <input type="checkbox" id="representativeName" />
                                <label htmlFor="representativeName">代表者名が必須</label>
                            </div>
                            <div>
                                <input type="checkbox" id="phoneNumber" />
                                <label htmlFor="phoneNumber">電話番号が必須</label>
                            </div>
                            <div>
                                <input type="checkbox" id="faxNumber" />
                                <label htmlFor="faxNumber">FAX番号が必須</label>
                            </div>
                            <div>
                                <input type="checkbox" id="websiteUrl" />
                                <label htmlFor="websiteUrl">サイトURLが必須</label>
                            </div>
                            <div>
                                <input type="checkbox" id="contactUrl" />
                                <label htmlFor="contactUrl">お問い合わせURLが必須</label>
                            </div>
                            <div>
                                <input type="checkbox" id="emailAddress" />
                                <label htmlFor="emailAddress">メールアドレスが必須</label>
                            </div>
                            <div>
                                <input type="checkbox" id="xUrl" />
                                <label htmlFor="xUrl">X(旧:Twitter)のURLが必須</label>
                            </div>
                            <div>
                                <input type="checkbox" id="facebookUrl" />
                                <label htmlFor="facebookUrl">FacebookのURLが必須</label>
                            </div>
                            <div>
                                <input type="checkbox" id="instagramUrl" />
                                <label htmlFor="instagramUrl">InstagramのURLが必須</label>
                            </div>
                        </div>
                        <p className="note">※団体名/所在地は100％付与されています。</p>
                        <a href="#" className="search-cta-button">この条件で検索</a>
                    </div>
                </div>
            )}
        </div>
    );
};

export default DetailSearchForm;
